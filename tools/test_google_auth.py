#!/usr/bin/env python3
"""
Test Google Cloud Authentication
Verifies that service account credentials are properly configured.

Usage:
    python test_google_auth.py
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for .env loading
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

def test_authentication():
    """Test Google Cloud service account authentication."""

    print("=" * 60)
    print("Testing Google Cloud Authentication")
    print("=" * 60)

    # Check environment variables
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    print(f"\n1. Environment Variables:")
    print(f"   Project ID: {project_id}")
    print(f"   Credentials Path: {credentials_path}")

    if not project_id or not credentials_path:
        print("\n❌ ERROR: Missing environment variables")
        print("   Make sure .env file exists and contains:")
        print("   - GOOGLE_CLOUD_PROJECT_ID")
        print("   - GOOGLE_APPLICATION_CREDENTIALS")
        return False

    # Check credentials file exists
    creds_file = Path(__file__).parent.parent / credentials_path
    print(f"\n2. Credentials File:")
    print(f"   Path: {creds_file}")
    print(f"   Exists: {creds_file.exists()}")

    if not creds_file.exists():
        print("\n❌ ERROR: Credentials file not found")
        return False

    # Test authentication with Google Drive API
    try:
        print("\n3. Testing Google Drive API authentication...")

        credentials = service_account.Credentials.from_service_account_file(
            str(creds_file),
            scopes=[
                'https://www.googleapis.com/auth/drive.readonly',
                'https://www.googleapis.com/auth/documents.readonly',
                'https://www.googleapis.com/auth/spreadsheets.readonly'
            ]
        )

        # Build Drive service
        drive_service = build('drive', 'v3', credentials=credentials)

        # Test API call - list first 5 files
        results = drive_service.files().list(
            pageSize=5,
            fields="files(id, name, mimeType)"
        ).execute()

        files = results.get('files', [])

        print("   ✓ Authentication successful!")
        print(f"   ✓ Service account: {credentials.service_account_email}")
        print(f"   ✓ Project: {project_id}")

        if files:
            print(f"\n4. Sample accessible files ({len(files)}):")
            for file in files:
                print(f"   - {file['name']} ({file['mimeType']})")
        else:
            print(f"\n4. No files accessible (this is OK for new service accounts)")

        print("\n" + "=" * 60)
        print("✅ SUCCESS: Google Cloud is properly configured!")
        print("=" * 60)

        return True

    except Exception as e:
        print(f"\n❌ ERROR: Authentication failed")
        print(f"   {str(e)}")
        return False

if __name__ == "__main__":
    success = test_authentication()
    sys.exit(0 if success else 1)
