#!/usr/bin/env python3
"""
Publish document to Google Docs via Drive API and share.
Uses Drive API instead of Docs API (more likely to be enabled).

Usage:
    python publish_via_drive.py --file PROJECT_OVERVIEW.md --email robert@antal.me
"""

import os
import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

load_dotenv()

def publish_and_share_via_drive(file_path: str, share_email: str, doc_title: str = None, role: str = 'writer'):
    """
    Upload file to Google Drive as Google Doc and share.

    Args:
        file_path: Path to text/markdown file
        share_email: Email to share document with
        doc_title: Title for the Google Doc (default: filename)
        role: Permission role ('reader', 'commenter', 'writer')
    """
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"❌ ERROR: File not found: {file_path}")
        return None

    print(f"\n📄 Uploading {file_path.name} to Google Docs via Drive API")
    print("=" * 60)

    # Authenticate
    print("1. Authenticating with Google Drive API...")
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not credentials_path:
        print("❌ ERROR: GOOGLE_APPLICATION_CREDENTIALS not set")
        return None

    creds_file = Path(__file__).parent.parent / credentials_path

    try:
        credentials = service_account.Credentials.from_service_account_file(
            str(creds_file),
            scopes=[
                'https://www.googleapis.com/auth/drive.file',
                'https://www.googleapis.com/auth/drive'
            ]
        )

        drive_service = build('drive', 'v3', credentials=credentials)
        print("   ✓ Authenticated successfully")
    except Exception as e:
        print(f"❌ ERROR: Authentication failed: {str(e)}")
        return None

    # Upload file as Google Doc
    print("\n2. Creating Google Doc...")
    document_title = doc_title or file_path.stem

    try:
        file_metadata = {
            'name': document_title,
            'mimeType': 'application/vnd.google-apps.document'
        }

        media = MediaFileUpload(
            str(file_path),
            mimetype='text/plain',
            resumable=True
        )

        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name, webViewLink'
        ).execute()

        doc_id = file.get('id')
        doc_url = file.get('webViewLink')

        print(f"   ✓ Created: {document_title}")
        print(f"   ✓ Document ID: {doc_id}")
    except Exception as e:
        print(f"❌ ERROR creating document: {str(e)}")
        return None

    # Share with email
    print(f"\n3. Sharing with {share_email}...")
    try:
        permission = {
            'type': 'user',
            'role': role,
            'emailAddress': share_email
        }

        drive_service.permissions().create(
            fileId=doc_id,
            body=permission,
            sendNotificationEmail=True,
            emailMessage=f"Here's the thesis project overview document: {document_title}"
        ).execute()

        print(f"   ✓ Shared with {share_email} (role: {role})")
    except Exception as e:
        print(f"⚠️  WARNING: Sharing failed: {str(e)}")
        print(f"   Document created but not shared")
        print(f"   You can manually share from the URL below")

    print("\n" + "=" * 60)
    print("✅ SUCCESS!")
    print("=" * 60)
    print(f"📄 Document URL: {doc_url}")
    print(f"📁 Document ID: {doc_id}")
    print(f"👤 Shared with: {share_email} ({role})")
    print(f"\n📧 {share_email} will receive an email notification.")
    print(f"\nℹ️  Note: Document is plain text. For formatted Markdown,")
    print(f"     enable Google Docs API in Cloud Console.")

    return doc_id

def main():
    parser = argparse.ArgumentParser(description="Publish and share via Drive API")
    parser.add_argument('--file', type=str, required=True, help="Path to file")
    parser.add_argument('--email', type=str, required=True, help="Email to share with")
    parser.add_argument('--title', type=str, help="Title for the document")
    parser.add_argument('--role', type=str, default='writer',
                        choices=['reader', 'commenter', 'writer'],
                        help="Permission role (default: writer)")

    args = parser.parse_args()
    publish_and_share_via_drive(args.file, args.email, args.title, args.role)

if __name__ == "__main__":
    main()
