#!/usr/bin/env python3
"""Check which organization the project belongs to."""

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
    creds_path = './credentials/google-service-account.json'

full_path = Path(__file__).parent.parent / creds_path

credentials = service_account.Credentials.from_service_account_file(
    str(full_path),
    scopes=['https://www.googleapis.com/auth/cloud-platform.read-only']
)

# Get project info
project_id = credentials.project_id

print(f"\n📊 Project Information")
print("=" * 60)
print(f"Project ID: {project_id}")
print(f"Service Account: {credentials.service_account_email}")

# Try to get project details
try:
    service = build('cloudresourcemanager', 'v1', credentials=credentials)

    project = service.projects().get(projectId=project_id).execute()

    print(f"\nProject Details:")
    print(f"  Name: {project.get('name', 'N/A')}")
    print(f"  Number: {project.get('projectNumber', 'N/A')}")
    print(f"  State: {project.get('lifecycleState', 'N/A')}")

    # Check parent (organization)
    parent = project.get('parent', {})
    if parent:
        print(f"\nParent Organization:")
        print(f"  Type: {parent.get('type', 'N/A')}")
        print(f"  ID: {parent.get('id', 'N/A')}")
    else:
        print(f"\n⚠️  No organization linked!")
        print(f"   Project is standalone (no pooled storage)")

except Exception as e:
    print(f"\n❌ Error: {e}")
    print(f"\nℹ️  Service account may not have permission to read project metadata.")

print("=" * 60)
