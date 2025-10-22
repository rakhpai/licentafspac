#!/usr/bin/env python3
"""
Check Drive quota and list files including trash and shared drives.
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

def check_quota():
    """Check quota with detailed information."""

    print("\n" + "=" * 80)
    print("GOOGLE DRIVE QUOTA & FILES DIAGNOSTIC")
    print("=" * 80)

    # Get credentials path
    creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    print(f"\n1. Credentials Path: {creds_path}")

    if creds_path:
        full_path = Path(__file__).parent.parent / creds_path
        print(f"   Full Path: {full_path}")
        print(f"   Exists: {full_path.exists()}")

    # Authenticate
    print("\n2. Authenticating...")
    try:
        credentials = service_account.Credentials.from_service_account_file(
            str(full_path),
            scopes=['https://www.googleapis.com/auth/drive']
        )

        print(f"   ✓ Service Account: {credentials.service_account_email}")
        print(f"   ✓ Project: {credentials.project_id}")

        service = build('drive', 'v3', credentials=credentials)

    except Exception as e:
        print(f"   ✗ Error: {e}")
        return

    # Get storage info
    print("\n3. Storage Quota:")
    try:
        about = service.about().get(fields="storageQuota,user").execute()

        quota = about.get('storageQuota', {})
        user = about.get('user', {})

        print(f"   Email: {user.get('emailAddress', 'Unknown')}")

        limit = quota.get('limit')
        usage = quota.get('usage')
        usage_drive = quota.get('usageInDrive')
        usage_trash = quota.get('usageInDriveTrash')

        print(f"   Limit: {limit if limit else 'Unlimited'}")
        print(f"   Usage Total: {usage if usage else '0'}")
        print(f"   Usage in Drive: {usage_drive if usage_drive else '0'}")
        print(f"   Usage in Trash: {usage_trash if usage_trash else '0'}")

    except Exception as e:
        print(f"   ✗ Error: {e}")

    # List regular files
    print("\n4. Regular Files:")
    try:
        results = service.files().list(
            pageSize=100,
            fields="files(id, name, mimeType, size, trashed)",
            q="trashed=false"
        ).execute()

        files = results.get('files', [])
        print(f"   Found: {len(files)} file(s)")

        if files:
            for f in files[:10]:  # Show first 10
                size = f.get('size', 'N/A')
                print(f"   - {f['name']} ({size} bytes)")

    except Exception as e:
        print(f"   ✗ Error: {e}")

    # List trashed files
    print("\n5. Trashed Files:")
    try:
        results = service.files().list(
            pageSize=100,
            fields="files(id, name, size)",
            q="trashed=true"
        ).execute()

        files = results.get('files', [])
        print(f"   Found: {len(files)} file(s) in trash")

        total_trash_size = 0
        if files:
            for f in files[:10]:  # Show first 10
                size = int(f.get('size', 0)) if f.get('size') else 0
                total_trash_size += size
                print(f"   - {f['name']} ({size} bytes)")

            print(f"\n   Total trash size: {total_trash_size} bytes")

    except Exception as e:
        print(f"   ✗ Error: {e}")

    # List shared drives
    print("\n6. Shared Drives:")
    try:
        results = service.drives().list(pageSize=10).execute()
        drives = results.get('drives', [])
        print(f"   Found: {len(drives)} shared drive(s)")

        if drives:
            for d in drives:
                print(f"   - {d['name']} (ID: {d['id']})")

    except Exception as e:
        print(f"   ✗ Error: {e}")

    print("\n" + "=" * 80)
    print("DIAGNOSTIC COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    check_quota()
