#!/usr/bin/env python3
"""
Publish document to Google Docs and share with specific email.

Usage:
    python publish_and_share.py --file PROJECT_OVERVIEW.md --email robert@antal.me
"""

import os
import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

def publish_and_share(file_path: str, share_email: str, doc_title: str = None, role: str = 'writer'):
    """
    Publish Markdown to Google Docs and share with email.

    Args:
        file_path: Path to Markdown file
        share_email: Email to share document with
        doc_title: Title for the Google Doc (default: filename)
        role: Permission role ('reader', 'commenter', 'writer')
    """
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"❌ ERROR: File not found: {file_path}")
        return None

    print(f"\n📄 Publishing {file_path.name} to Google Docs")
    print("=" * 60)

    # Read markdown file
    print("1. Reading file...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"   ✓ Read {len(content)} characters")
    except Exception as e:
        print(f"❌ ERROR reading file: {str(e)}")
        return None

    # Authenticate
    print("\n2. Authenticating with Google APIs...")
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not credentials_path:
        print("❌ ERROR: GOOGLE_APPLICATION_CREDENTIALS not set")
        return None

    creds_file = Path(__file__).parent.parent / credentials_path

    try:
        credentials = service_account.Credentials.from_service_account_file(
            str(creds_file),
            scopes=[
                'https://www.googleapis.com/auth/documents',
                'https://www.googleapis.com/auth/drive.file',
                'https://www.googleapis.com/auth/drive'
            ]
        )

        docs_service = build('docs', 'v1', credentials=credentials)
        drive_service = build('drive', 'v3', credentials=credentials)

        print("   ✓ Authenticated successfully")
    except Exception as e:
        print(f"❌ ERROR: Authentication failed: {str(e)}")
        return None

    # Create document
    print("\n3. Creating Google Doc...")
    document_title = doc_title or file_path.stem

    try:
        document = {'title': document_title}
        doc = docs_service.documents().create(body=document).execute()
        doc_id = doc.get('documentId')

        print(f"   ✓ Created: {document_title}")
        print(f"   ✓ Document ID: {doc_id}")
    except Exception as e:
        print(f"❌ ERROR creating document: {str(e)}")
        return None

    # Insert content
    print("\n4. Inserting content...")
    try:
        requests = [{
            'insertText': {
                'location': {'index': 1},
                'text': content
            }
        }]

        docs_service.documents().batchUpdate(
            documentId=doc_id,
            body={'requests': requests}
        ).execute()

        print("   ✓ Content inserted")
    except Exception as e:
        print(f"❌ ERROR inserting content: {str(e)}")
        return None

    # Share with email
    print(f"\n5. Sharing with {share_email}...")
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
        print(f"❌ ERROR sharing document: {str(e)}")
        print(f"   Document still created, but sharing failed")

    # Get document URL
    doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"

    print("\n" + "=" * 60)
    print("✅ SUCCESS!")
    print("=" * 60)
    print(f"📄 Document URL: {doc_url}")
    print(f"📁 Document ID: {doc_id}")
    print(f"👤 Shared with: {share_email} ({role})")
    print(f"\n📧 {share_email} will receive an email notification with the link.")

    return doc_id

def main():
    parser = argparse.ArgumentParser(description="Publish and share document to Google Docs")
    parser.add_argument('--file', type=str, required=True, help="Path to Markdown file")
    parser.add_argument('--email', type=str, required=True, help="Email to share with")
    parser.add_argument('--title', type=str, help="Title for the Google Doc (default: filename)")
    parser.add_argument('--role', type=str, default='writer',
                        choices=['reader', 'commenter', 'writer'],
                        help="Permission role (default: writer)")

    args = parser.parse_args()
    publish_and_share(args.file, args.email, args.title, args.role)

if __name__ == "__main__":
    main()
