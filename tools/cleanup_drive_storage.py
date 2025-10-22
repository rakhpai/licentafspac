#!/usr/bin/env python3
"""
Clean up Google Drive storage for service account.

Lists all files owned by the service account and allows deletion
to free up storage quota.

Usage:
    # List all files
    python cleanup_drive_storage.py --list

    # Delete specific file by ID
    python cleanup_drive_storage.py --delete FILE_ID

    # Delete all files (DANGEROUS - asks for confirmation)
    python cleanup_drive_storage.py --delete-all

    # List files with size information
    python cleanup_drive_storage.py --list --show-size

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

load_dotenv()

def get_drive_service():
    """Get authenticated Drive service."""
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not credentials_path:
        print("❌ ERROR: GOOGLE_APPLICATION_CREDENTIALS not set")
        return None

    creds_file = Path(__file__).parent.parent / credentials_path

    try:
        credentials = service_account.Credentials.from_service_account_file(
            str(creds_file),
            scopes=['https://www.googleapis.com/auth/drive']
        )

        service = build('drive', 'v3', credentials=credentials)
        return service
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return None

def format_size(size_bytes):
    """Format bytes to human-readable size."""
    if size_bytes is None:
        return "N/A"

    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def list_files(service, show_size=False):
    """List all files in Drive."""
    print("\n📁 Listing files in Google Drive...")
    print("=" * 80)

    try:
        # Get all files
        results = service.files().list(
            pageSize=100,
            fields="files(id, name, mimeType, size, createdTime, modifiedTime)",
            orderBy="quotaBytesUsed desc"
        ).execute()

        files = results.get('files', [])

        if not files:
            print("✅ No files found. Drive is empty!")
            return []

        print(f"Found {len(files)} file(s):\n")

        total_size = 0

        for i, file in enumerate(files, 1):
            file_id = file['id']
            name = file['name']
            mime_type = file['mimeType']
            size = file.get('size')
            created = file.get('createdTime', 'Unknown')[:10]
            modified = file.get('modifiedTime', 'Unknown')[:10]

            # Add to total
            if size:
                total_size += int(size)

            # Format output
            type_short = mime_type.split('.')[-1] if '.' in mime_type else mime_type

            print(f"{i}. {name}")
            print(f"   ID: {file_id}")
            print(f"   Type: {type_short}")

            if show_size and size:
                print(f"   Size: {format_size(int(size))}")

            print(f"   Created: {created}, Modified: {modified}")
            print()

        if show_size:
            print("=" * 80)
            print(f"Total storage used: {format_size(total_size)}")

        print("=" * 80)

        return files

    except Exception as e:
        print(f"❌ ERROR listing files: {str(e)}")
        return []

def delete_file(service, file_id):
    """Delete a specific file by ID."""
    try:
        # Get file info first
        file = service.files().get(fileId=file_id, fields="name").execute()
        file_name = file.get('name', 'Unknown')

        # Delete
        service.files().delete(fileId=file_id).execute()
        print(f"✅ Deleted: {file_name} (ID: {file_id})")
        return True

    except Exception as e:
        print(f"❌ ERROR deleting file {file_id}: {str(e)}")
        return False

def delete_all_files(service):
    """Delete all files (with confirmation)."""
    print("\n⚠️  WARNING: This will delete ALL files in the service account's Drive!")
    print("=" * 80)

    # List files first
    files = list_files(service)

    if not files:
        print("No files to delete.")
        return

    print(f"\n⚠️  About to delete {len(files)} file(s)!")
    confirm = input("Type 'DELETE ALL' to confirm: ")

    if confirm != "DELETE ALL":
        print("❌ Cancelled. No files deleted.")
        return

    print("\n🗑️  Deleting files...")

    deleted = 0
    failed = 0

    for file in files:
        file_id = file['id']
        file_name = file['name']

        try:
            service.files().delete(fileId=file_id).execute()
            print(f"  ✓ Deleted: {file_name}")
            deleted += 1
        except Exception as e:
            print(f"  ✗ Failed: {file_name} ({str(e)})")
            failed += 1

    print("\n" + "=" * 80)
    print(f"✅ Deleted: {deleted} file(s)")
    if failed > 0:
        print(f"❌ Failed: {failed} file(s)")
    print("=" * 80)

def get_storage_info(service):
    """Get storage quota information."""
    try:
        about = service.about().get(fields="storageQuota, user").execute()

        quota = about.get('storageQuota', {})
        user = about.get('user', {})

        limit = int(quota.get('limit', 0))
        usage = int(quota.get('usage', 0))
        usage_in_drive = int(quota.get('usageInDrive', 0))

        print("\n📊 Storage Information")
        print("=" * 80)
        print(f"User: {user.get('emailAddress', 'Unknown')}")
        print(f"Total Quota: {format_size(limit)}")
        print(f"Used: {format_size(usage)} ({usage/limit*100:.1f}%)" if limit > 0 else "Used: Unknown")
        print(f"Used in Drive: {format_size(usage_in_drive)}")

        if limit > 0:
            remaining = limit - usage
            print(f"Remaining: {format_size(remaining)}")

            if usage >= limit:
                print("\n⚠️  QUOTA EXCEEDED! Delete files to free up space.")
            elif usage > limit * 0.9:
                print("\n⚠️  WARNING: Over 90% of quota used.")

        print("=" * 80)

    except Exception as e:
        print(f"❌ ERROR getting storage info: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Clean up Google Drive storage")
    parser.add_argument('--list', action='store_true', help="List all files")
    parser.add_argument('--show-size', action='store_true', help="Show file sizes")
    parser.add_argument('--delete', type=str, metavar='FILE_ID', help="Delete specific file by ID")
    parser.add_argument('--delete-all', action='store_true', help="Delete all files (dangerous!)")
    parser.add_argument('--info', action='store_true', help="Show storage quota information")

    args = parser.parse_args()

    # Get Drive service
    service = get_drive_service()
    if not service:
        return

    # Show storage info
    if args.info or not any([args.list, args.delete, args.delete_all]):
        get_storage_info(service)

    # List files
    if args.list:
        list_files(service, show_size=args.show_size)

    # Delete specific file
    if args.delete:
        delete_file(service, args.delete)

    # Delete all files
    if args.delete_all:
        delete_all_files(service)

if __name__ == "__main__":
    main()
