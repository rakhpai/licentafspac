#!/usr/bin/env python3
"""
Export Data to Google Sheets

Export questionnaire responses, interview data, or analysis results to Google Sheets
for easy sharing with thesis supervisor and committee.

Usage:
    python export_to_sheets.py --file data.csv --title "Survey Responses"
    python export_to_sheets.py --file analysis.xlsx --sheet-name "Results"

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
import pandas as pd

load_dotenv()

def export_to_sheets(file_path: str, sheet_title: str = None, sheet_name: str = None):
    """
    Export data file to Google Sheets.

    Args:
        file_path: Path to CSV or Excel file
        sheet_title: Title for the new Google Sheet
        sheet_name: Name of sheet tab within the spreadsheet
    """
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"❌ ERROR: File not found: {file_path}")
        return None

    print(f"\n📊 Exporting {file_path.name} to Google Sheets")
    print("=" * 60)

    # Load data
    print("1. Loading data...")
    try:
        if file_path.suffix == '.csv':
            df = pd.read_csv(file_path)
        elif file_path.suffix in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path, sheet_name=sheet_name or 0)
        else:
            print(f"❌ ERROR: Unsupported file type: {file_path.suffix}")
            print("   Supported: .csv, .xlsx, .xls")
            return None

        print(f"   ✓ Loaded {len(df)} rows, {len(df.columns)} columns")

    except Exception as e:
        print(f"❌ ERROR loading file: {str(e)}")
        return None

    # Authenticate
    print("\n2. Authenticating with Google Sheets API...")
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not credentials_path:
        print("❌ ERROR: GOOGLE_APPLICATION_CREDENTIALS not set")
        return None

    creds_file = Path(__file__).parent.parent / credentials_path

    try:
        credentials = service_account.Credentials.from_service_account_file(
            str(creds_file),
            scopes=[
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive.file'
            ]
        )

        sheets_service = build('sheets', 'v4', credentials=credentials)
        drive_service = build('drive', 'v3', credentials=credentials)

        print("   ✓ Authenticated successfully")

    except Exception as e:
        print(f"❌ ERROR: Authentication failed: {str(e)}")
        return None

    # Create new spreadsheet
    print("\n3. Creating Google Sheet...")
    spreadsheet_title = sheet_title or file_path.stem

    try:
        spreadsheet = {
            'properties': {
                'title': spreadsheet_title
            }
        }

        spreadsheet = sheets_service.spreadsheets().create(
            body=spreadsheet,
            fields='spreadsheetId'
        ).execute()

        spreadsheet_id = spreadsheet.get('spreadsheetId')
        print(f"   ✓ Created spreadsheet: {spreadsheet_title}")
        print(f"   ✓ Spreadsheet ID: {spreadsheet_id}")

    except Exception as e:
        print(f"❌ ERROR creating spreadsheet: {str(e)}")
        return None

    # Prepare data for Sheets API
    print("\n4. Uploading data...")

    # Convert DataFrame to list of lists (including header)
    values = [df.columns.tolist()] + df.values.tolist()

    # Convert NaN to empty string
    values = [['' if pd.isna(cell) else cell for cell in row] for row in values]

    body = {
        'values': values
    }

    try:
        result = sheets_service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range='A1',
            valueInputOption='RAW',
            body=body
        ).execute()

        print(f"   ✓ Updated {result.get('updatedCells')} cells")

        # Format header row
        requests = [{
            'repeatCell': {
                'range': {
                    'sheetId': 0,
                    'startRowIndex': 0,
                    'endRowIndex': 1
                },
                'cell': {
                    'userEnteredFormat': {
                        'backgroundColor': {'red': 0.2, 'green': 0.2, 'blue': 0.2},
                        'textFormat': {
                            'foregroundColor': {'red': 1, 'green': 1, 'blue': 1},
                            'bold': True
                        }
                    }
                },
                'fields': 'userEnteredFormat(backgroundColor,textFormat)'
            }
        }, {
            'autoResizeDimensions': {
                'dimensions': {
                    'sheetId': 0,
                    'dimension': 'COLUMNS',
                    'startIndex': 0,
                    'endIndex': len(df.columns)
                }
            }
        }]

        sheets_service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={'requests': requests}
        ).execute()

        print("   ✓ Formatted header row")

    except Exception as e:
        print(f"❌ ERROR uploading data: {str(e)}")
        return None

    # Generate shareable link
    print("\n5. Generating shareable link...")
    sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit"

    print("\n" + "=" * 60)
    print("✅ SUCCESS!")
    print("=" * 60)
    print(f"📊 Spreadsheet URL: {sheet_url}")
    print(f"📁 Spreadsheet ID: {spreadsheet_id}")
    print(f"📈 Data: {len(df)} rows × {len(df.columns)} columns")
    print("\nℹ️  To share with supervisor:")
    print("   1. Open the URL above")
    print("   2. Click 'Share' button")
    print("   3. Add supervisor's email with 'Viewer' or 'Commenter' access")

    return spreadsheet_id

def main():
    parser = argparse.ArgumentParser(description="Export data to Google Sheets")
    parser.add_argument('--file', type=str, required=True, help="Path to CSV or Excel file")
    parser.add_argument('--title', type=str, help="Title for the Google Sheet (default: filename)")
    parser.add_argument('--sheet-name', type=str, help="Sheet name within Excel file (default: first sheet)")

    args = parser.parse_args()
    export_to_sheets(args.file, args.title, args.sheet_name)

if __name__ == "__main__":
    main()
