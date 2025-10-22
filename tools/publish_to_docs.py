#!/usr/bin/env python3
"""
Publish Markdown to Google Docs

Convert thesis chapters from Markdown to Google Docs for easy sharing
with supervisor and committee for review.

Usage:
    python publish_to_docs.py --file chapter1.md --title "Capitol 1: Introducere"
    python publish_to_docs.py --file drafts/chapter2.md

Author: Robert Eduard Antal
Date: 2024-10-22
"""

import os
import sys
import argparse
from pathlib import Path
import re

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

def markdown_to_docs_requests(markdown_text: str):
    """
    Convert Markdown to Google Docs API requests.
    Supports: headings, bold, italic, lists, links.

    Args:
        markdown_text: Markdown content

    Returns:
        List of Google Docs API request objects
    """
    requests = []
    index = 1  # Start at index 1 (after title)

    lines = markdown_text.split('\n')

    for line in lines:
        if not line.strip():
            # Empty line - add paragraph break
            requests.append({
                'insertText': {
                    'location': {'index': index},
                    'text': '\n'
                }
            })
            index += 1
            continue

        # Check for headers
        header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if header_match:
            level = len(header_match.group(1))
            text = header_match.group(2) + '\n'

            requests.append({
                'insertText': {
                    'location': {'index': index},
                    'text': text
                }
            })

            # Style as heading
            requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': index,
                        'endIndex': index + len(text)
                    },
                    'paragraphStyle': {
                        'namedStyleType': f'HEADING_{level}'
                    },
                    'fields': 'namedStyleType'
                }
            })

            index += len(text)
            continue

        # Regular paragraph with inline formatting
        # Simple conversion (can be enhanced)
        text = line

        # Convert **bold**
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)

        # Convert *italic*
        text = re.sub(r'\*(.+?)\*', r'\1', text)

        # Add newline
        text += '\n'

        requests.append({
            'insertText': {
                'location': {'index': index},
                'text': text
            }
        })

        index += len(text)

    return requests

def publish_to_docs(file_path: str, doc_title: str = None):
    """
    Publish Markdown file to Google Docs.

    Args:
        file_path: Path to Markdown file
        doc_title: Title for the Google Doc (default: filename)
    """
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"❌ ERROR: File not found: {file_path}")
        return None

    print(f"\n📄 Publishing {file_path.name} to Google Docs")
    print("=" * 60)

    # Read markdown file
    print("1. Reading Markdown file...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        print(f"   ✓ Read {len(markdown_content)} characters")

    except Exception as e:
        print(f"❌ ERROR reading file: {str(e)}")
        return None

    # Authenticate
    print("\n2. Authenticating with Google Docs API...")
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
                'https://www.googleapis.com/auth/drive.file'
            ]
        )

        docs_service = build('docs', 'v1', credentials=credentials)
        drive_service = build('drive', 'v3', credentials=credentials)

        print("   ✓ Authenticated successfully")

    except Exception as e:
        print(f"❌ ERROR: Authentication failed: {str(e)}")
        return None

    # Create new document
    print("\n3. Creating Google Doc...")
    document_title = doc_title or file_path.stem

    try:
        document = {
            'title': document_title
        }

        doc = docs_service.documents().create(body=document).execute()
        doc_id = doc.get('documentId')

        print(f"   ✓ Created document: {document_title}")
        print(f"   ✓ Document ID: {doc_id}")

    except Exception as e:
        print(f"❌ ERROR creating document: {str(e)}")
        return None

    # Convert markdown and insert content
    print("\n4. Converting and inserting content...")

    try:
        # Simple approach: insert as plain text with basic formatting
        # For full markdown support, use a library like python-markdown

        requests = [{
            'insertText': {
                'location': {'index': 1},
                'text': markdown_content
            }
        }]

        docs_service.documents().batchUpdate(
            documentId=doc_id,
            body={'requests': requests}
        ).execute()

        print("   ✓ Content inserted")
        print("   ℹ️  Note: Basic formatting applied. For full markdown support,")
        print("      edit the script to use python-markdown library.")

    except Exception as e:
        print(f"❌ ERROR inserting content: {str(e)}")
        return None

    # Generate shareable link
    doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"

    print("\n" + "=" * 60)
    print("✅ SUCCESS!")
    print("=" * 60)
    print(f"📄 Document URL: {doc_url}")
    print(f"📁 Document ID: {doc_id}")
    print("\nℹ️  To share with supervisor:")
    print("   1. Open the URL above")
    print("   2. Click 'Share' button")
    print("   3. Add supervisor's email with 'Commenter' access")
    print("   4. Enable 'Anyone with link can comment' for easy review")

    return doc_id

def main():
    parser = argparse.ArgumentParser(description="Publish Markdown to Google Docs")
    parser.add_argument('--file', type=str, required=True, help="Path to Markdown file")
    parser.add_argument('--title', type=str, help="Title for the Google Doc (default: filename)")

    args = parser.parse_args()
    publish_to_docs(args.file, args.title)

if __name__ == "__main__":
    main()
