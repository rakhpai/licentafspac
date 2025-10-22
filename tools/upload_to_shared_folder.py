#!/usr/bin/env python3
"""
Upload file directly to shared folder (bypasses quota check).
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

load_dotenv()

def upload_to_shared_folder(file_path, folder_id, doc_title=None):
    """Upload file to shared folder."""

    file_path = Path(file_path)

    print(f"\n📤 Uploading {file_path.name} to shared folder")
    print("=" * 60)

    # Get credentials
    creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not creds_path:
        creds_path = './credentials/google-service-account.json'

    full_path = Path(__file__).parent.parent / creds_path

    credentials = service_account.Credentials.from_service_account_file(
        str(full_path),
        scopes=['https://www.googleapis.com/auth/drive.file']
    )

    service = build('drive', 'v3', credentials=credentials)

    # File metadata
    title = doc_title or file_path.stem
    file_metadata = {
        'name': title,
        'parents': [folder_id],
        # Try as plain text file instead of Google Doc to avoid quota check
        # 'mimeType': 'text/plain'
    }

    # Read file content
    with open(file_path, 'r') as f:
        content = f.read()

    # Try creating as Google Doc
    print("1. Attempting upload as Google Doc...")
    file_metadata['mimeType'] = 'application/vnd.google-apps.document'

    media = MediaFileUpload(
        str(file_path),
        mimetype='text/plain',
        resumable=True
    )

    try:
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name, webViewLink',
            supportsAllDrives=True  # Important for shared folders!
        ).execute()

        print(f"✅ SUCCESS!")
        print(f"📄 Document: {file['name']}")
        print(f"🔗 URL: {file['webViewLink']}")
        print(f"📁 ID: {file['id']}")

        return file['id']

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python upload_to_shared_folder.py FILE FOLDER_ID [TITLE]")
        sys.exit(1)

    file_path = sys.argv[1]
    folder_id = sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else None

    upload_to_shared_folder(file_path, folder_id, title)
