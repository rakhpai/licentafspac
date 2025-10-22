#!/usr/bin/env python3
"""Force cleanup all files from Drive (no confirmation)."""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
if not creds_path:
    creds_path = sys.argv[1] if len(sys.argv) > 1 else './credentials/google-service-account.json'

full_path = Path(__file__).parent.parent / creds_path

credentials = service_account.Credentials.from_service_account_file(
    str(full_path),
    scopes=['https://www.googleapis.com/auth/drive']
)

service = build('drive', 'v3', credentials=credentials)

print("Fetching files...")
results = service.files().list(
    pageSize=1000,
    fields="files(id, name)"
).execute()

files = results.get('files', [])
print(f"Found {len(files)} files")

deleted = 0
for file in files:
    try:
        service.files().delete(fileId=file['id']).execute()
        print(f"✓ Deleted: {file['name']}")
        deleted += 1
    except Exception as e:
        print(f"✗ Failed: {file['name']} - {e}")

print(f"\n✅ Deleted {deleted}/{len(files)} files")
