#!/usr/bin/env python3
"""Share a Google Drive document with an email address."""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

def share_document(file_id, email, role='writer'):
    """Share a document with an email address."""

    print(f"\n📤 Sharing document with {email}")
    print("=" * 60)

    # Get credentials
    creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not creds_path:
        creds_path = './credentials/google-service-account.json'

    full_path = Path(__file__).parent.parent / creds_path

    credentials = service_account.Credentials.from_service_account_file(
        str(full_path),
        scopes=['https://www.googleapis.com/auth/drive']
    )

    service = build('drive', 'v3', credentials=credentials)

    try:
        permission = {
            'type': 'user',
            'role': role,
            'emailAddress': email
        }

        result = service.permissions().create(
            fileId=file_id,
            body=permission,
            sendNotificationEmail=True,
            supportsAllDrives=True,
            emailMessage=f"Here's the thesis overview document. You have {role} access."
        ).execute()

        print(f"✅ SUCCESS!")
        print(f"👤 Shared with: {email}")
        print(f"🔑 Role: {role}")
        print(f"📧 Notification email sent")
        print(f"📄 File ID: {file_id}")

        return True

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python share_document.py FILE_ID EMAIL [ROLE]")
        sys.exit(1)

    file_id = sys.argv[1]
    email = sys.argv[2]
    role = sys.argv[3] if len(sys.argv) > 3 else 'writer'

    share_document(file_id, email, role)
