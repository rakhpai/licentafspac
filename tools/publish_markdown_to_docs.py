#!/usr/bin/env python3
"""
Publish Markdown to Google Docs with proper formatting.

Uses markgdoc library to convert Markdown with full formatting support:
- Headings (H1-H6)
- Bold, italic, strikethrough
- Lists (bullet and numbered)
- Links
- Tables
- Horizontal rules

Usage:
    python publish_markdown_to_docs.py \\
      --file PROJECT_OVERVIEW.md \\
      --title "Lucrare de Licență - Overview" \\
      --folder-id 0APsOGraGUhOQUk9PVA \\
      --share robert@antal.me

Author: Robert Eduard Antal
Date: 2024-10-22
"""

import os
import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Import markgdoc functions
try:
    from markgdoc import convert_to_google_docs
    MARKGDOC_AVAILABLE = True
except ImportError:
    print("❌ ERROR: markgdoc library not installed")
    print("   Install with: pip install markgdoc")
    MARKGDOC_AVAILABLE = False

load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
]

def publish_markdown_to_docs(
    file_path: str,
    doc_title: str = None,
    folder_id: str = None,
    share_email: str = None,
    share_role: str = 'writer'
):
    """
    Publish Markdown file to Google Docs with proper formatting.

    Args:
        file_path: Path to Markdown file
        doc_title: Title for the Google Doc (default: filename)
        folder_id: Google Drive folder/Shared Drive ID (optional)
        share_email: Email to share document with (optional)
        share_role: Permission role ('reader', 'commenter', 'writer')

    Returns:
        Document ID if successful, None otherwise
    """

    if not MARKGDOC_AVAILABLE:
        return None

    file_path = Path(file_path)

    if not file_path.exists():
        print(f"❌ ERROR: File not found: {file_path}")
        return None

    print(f"\n📝 Publishing {file_path.name} to Google Docs")
    print("=" * 80)

    # Read markdown content
    print("1. Reading Markdown file...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        print(f"   ✓ Read {len(markdown_content)} characters")
        print(f"   ✓ File: {file_path}")

    except Exception as e:
        print(f"❌ ERROR reading file: {str(e)}")
        return None

    # Set document title
    document_title = doc_title or file_path.stem
    print(f"\n2. Document title: {document_title}")

    # Authenticate
    print("\n3. Authenticating with Google APIs...")
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not credentials_path:
        print("❌ ERROR: GOOGLE_APPLICATION_CREDENTIALS not set in .env")
        return None

    creds_file = Path(__file__).parent.parent / credentials_path

    if not creds_file.exists():
        print(f"❌ ERROR: Credentials file not found: {creds_file}")
        return None

    try:
        credentials = service_account.Credentials.from_service_account_file(
            str(creds_file),
            scopes=SCOPES
        )

        docs_service = build('docs', 'v1', credentials=credentials)
        drive_service = build('drive', 'v3', credentials=credentials)

        print(f"   ✓ Service Account: {credentials.service_account_email}")
        print(f"   ✓ Project: {credentials.project_id}")

    except Exception as e:
        print(f"❌ ERROR: Authentication failed: {str(e)}")
        return None

    # Convert Markdown to Google Docs using markgdoc
    print("\n4. Converting Markdown to Google Docs...")
    print("   ℹ️  Using markgdoc library for formatting")

    try:
        # markgdoc's convert_to_google_docs function
        # Returns the Google Docs URL
        google_docs_url = convert_to_google_docs(
            markdown_content,
            document_title,
            docs_service,
            str(creds_file),
            SCOPES,
            debug=False  # Set to True for debugging
        )

        print(f"   ✓ Document created successfully!")

        # Extract document ID from URL
        # URL format: https://docs.google.com/document/d/{doc_id}/edit
        if '/d/' in google_docs_url:
            doc_id = google_docs_url.split('/d/')[1].split('/')[0]
        else:
            doc_id = google_docs_url

        print(f"   ✓ Document ID: {doc_id}")

    except Exception as e:
        print(f"❌ ERROR converting to Google Docs: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

    # Move to folder if specified
    if folder_id:
        print(f"\n5. Moving to folder/Shared Drive: {folder_id}...")
        try:
            # Get current parents
            file = drive_service.files().get(
                fileId=doc_id,
                fields='parents',
                supportsAllDrives=True
            ).execute()

            previous_parents = ','.join(file.get('parents', []))

            # Move to new parent
            drive_service.files().update(
                fileId=doc_id,
                addParents=folder_id,
                removeParents=previous_parents,
                fields='id, parents',
                supportsAllDrives=True
            ).execute()

            print(f"   ✓ Moved to folder: {folder_id}")

        except Exception as e:
            print(f"⚠️  WARNING: Could not move to folder: {str(e)}")
            print(f"   Document created but remains in root")

    # Share with email if specified
    if share_email:
        print(f"\n6. Sharing with {share_email}...")
        try:
            permission = {
                'type': 'user',
                'role': share_role,
                'emailAddress': share_email
            }

            drive_service.permissions().create(
                fileId=doc_id,
                body=permission,
                sendNotificationEmail=True,
                supportsAllDrives=True,
                emailMessage=f"Here's the document: {document_title}"
            ).execute()

            print(f"   ✓ Shared with: {share_email}")
            print(f"   ✓ Role: {share_role}")
            print(f"   ✓ Notification email sent")

        except Exception as e:
            print(f"⚠️  WARNING: Sharing failed: {str(e)}")
            print(f"   You can manually share from the URL below")

    # Final output
    print("\n" + "=" * 80)
    print("✅ SUCCESS!")
    print("=" * 80)
    print(f"📄 Document: {document_title}")
    print(f"🔗 URL: {google_docs_url}")
    print(f"📁 Document ID: {doc_id}")

    if folder_id:
        print(f"📂 Location: Shared Drive/Folder {folder_id}")

    if share_email:
        print(f"👤 Shared with: {share_email} ({share_role})")

    print(f"\n📊 Formatting applied:")
    print(f"   ✓ Headings (H1-H6)")
    print(f"   ✓ Bold, italic, strikethrough")
    print(f"   ✓ Lists (bullet and numbered)")
    print(f"   ✓ Links (clickable)")
    print(f"   ✓ Tables")
    print(f"   ✓ Horizontal rules")

    print("\n" + "=" * 80)

    return doc_id

def main():
    parser = argparse.ArgumentParser(
        description="Publish Markdown to Google Docs with proper formatting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python publish_markdown_to_docs.py --file chapter1.md --title "Chapter 1"

  # Upload to Shared Drive
  python publish_markdown_to_docs.py \\
    --file PROJECT_OVERVIEW.md \\
    --title "Thesis Overview" \\
    --folder-id 0APsOGraGUhOQUk9PVA

  # Upload and share
  python publish_markdown_to_docs.py \\
    --file chapter1.md \\
    --title "Chapter 1" \\
    --share robert@antal.me \\
    --role commenter
        """
    )

    parser.add_argument(
        '--file',
        type=str,
        required=True,
        help="Path to Markdown file"
    )

    parser.add_argument(
        '--title',
        type=str,
        help="Title for the Google Doc (default: filename)"
    )

    parser.add_argument(
        '--folder-id',
        type=str,
        help="Google Drive folder/Shared Drive ID to upload to"
    )

    parser.add_argument(
        '--share',
        type=str,
        dest='share_email',
        help="Email address to share document with"
    )

    parser.add_argument(
        '--role',
        type=str,
        default='writer',
        choices=['reader', 'commenter', 'writer'],
        help="Permission role for shared user (default: writer)"
    )

    args = parser.parse_args()

    # Publish the document
    doc_id = publish_markdown_to_docs(
        file_path=args.file,
        doc_title=args.title,
        folder_id=args.folder_id,
        share_email=args.share_email,
        share_role=args.role
    )

    # Exit with appropriate code
    sys.exit(0 if doc_id else 1)

if __name__ == "__main__":
    main()
