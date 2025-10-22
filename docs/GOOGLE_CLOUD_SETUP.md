# Google Cloud Setup Guide

**Project:** Lucrare de Licență - AI în Agențiile de Publicitate
**Student:** Robert Eduard Antal
**Date:** 2024-10-22

---

## 📋 Overview

This project uses Google Cloud Platform (GCP) for automating thesis-related tasks:

- **Google Forms** - Create and deploy questionnaires
- **Google Sheets** - Export and analyze survey data
- **Google Docs** - Publish chapters for supervisor review
- **Google Drive** - Share files and collaborate

**Google Cloud Project:** `fspac-2025-study-tools`
**Service Account:** `fspac-study-tools@fspac-2025-study-tools.iam.gserviceaccount.com`

---

## ⚙️ Setup Instructions

### 1. Prerequisites

Ensure you have:
- Python 3.8+ installed
- pip (Python package manager)
- Git repository initialized

### 2. Install Dependencies

```bash
cd /home/antal/projects/licentafspac
pip install -r tools/requirements.txt
```

This installs:
- Google API Python Client
- Authentication libraries
- Pandas for data processing
- OpenAI/Anthropic SDKs (optional, for qualitative analysis)

### 3. Verify Credentials

The credentials are already set up:

```bash
# .env file contains:
GOOGLE_CLOUD_PROJECT_ID=fspac-2025-study-tools
GOOGLE_APPLICATION_CREDENTIALS=./credentials/google-service-account.json
```

File permissions:
```bash
-rw-------  # credentials/google-service-account.json (chmod 600)
-rw-------  # .env (chmod 600)
```

### 4. Test Authentication

Run the authentication test script:

```bash
cd /home/antal/projects/licentafspac
python tools/test_google_auth.py
```

Expected output:
```
✅ SUCCESS: Google Cloud is properly configured!
✓ Service account: fspac-study-tools@...
✓ Project: fspac-2025-study-tools
```

---

## 🔧 Available Tools

### 1. Test Authentication
**Script:** `tools/test_google_auth.py`

Verifies Google Cloud credentials and API access.

```bash
python tools/test_google_auth.py
```

---

### 2. Create Google Forms
**Script:** `tools/create_google_form.py`

Create questionnaires for each thesis theme.

**Usage:**
```bash
# Theme 1: Transformarea proceselor prin AI
python tools/create_google_form.py --theme 1

# Theme 2: Competențe și skills gap
python tools/create_google_form.py --theme 2

# Theme 3: ROI și metrici de performanță
python tools/create_google_form.py --theme 3
```

**Output:**
- Creates a new Google Form
- Returns form ID and edit URL
- Displays question template to add manually

**Note:** Google Forms API has limitations. Questions need to be added manually via the web interface. The script provides the complete template.

---

### 3. Export Data to Google Sheets
**Script:** `tools/export_to_sheets.py`

Export CSV/Excel data to Google Sheets for sharing.

**Usage:**
```bash
# Export survey responses
python tools/export_to_sheets.py \
  --file tema1_transformare_procese/04_data_collection/aggregated_results.csv \
  --title "Survey Responses - Tema 1"

# Export analysis results
python tools/export_to_sheets.py \
  --file tema2_competente_viitor/05_analysis/skills_gap_matrix.xlsx \
  --sheet-name "Gap Analysis"
```

**Features:**
- Converts CSV/Excel to Google Sheets
- Auto-formats header row (dark background, bold)
- Auto-resizes columns
- Returns shareable link

**Output:**
```
✅ SUCCESS!
📊 Spreadsheet URL: https://docs.google.com/spreadsheets/d/[ID]/edit
```

---

### 4. Publish Markdown to Google Docs
**Script:** `tools/publish_to_docs.py`

Convert thesis chapters from Markdown to Google Docs for supervisor review.

**Usage:**
```bash
# Publish a chapter
python tools/publish_to_docs.py \
  --file tema1_transformare_procese/03_writing/chapter1_introduction.md \
  --title "Capitol 1: Introducere - Tema 1"

# Publish draft
python tools/publish_to_docs.py \
  --file drafts/literature_review.md \
  --title "Review Bibliografie - Draft"
```

**Features:**
- Converts Markdown to Google Docs
- Preserves basic formatting
- Creates shareable link

**Output:**
```
✅ SUCCESS!
📄 Document URL: https://docs.google.com/document/d/[ID]/edit
```

---

## 🔐 Security Best Practices

### ✅ DO:
1. **Keep credentials private**
   - `.env` and `credentials/` are in `.gitignore`
   - Never commit these files to git
   - Never share credentials publicly

2. **Use secure permissions**
   - `.env` → `chmod 600` (owner read/write only)
   - `credentials/*.json` → `chmod 600`

3. **Limit access**
   - Only use service accounts (not personal accounts)
   - Grant minimum necessary scopes
   - Rotate credentials if compromised

4. **Data protection**
   - Never commit sensitive data (interviews, personal info)
   - Use anonymized/aggregated data when sharing
   - Follow GDPR guidelines

### ❌ DON'T:
1. Don't commit `.env` or `credentials/` to git
2. Don't share API keys in screenshots or logs
3. Don't use production credentials for testing
4. Don't grant excessive API scopes
5. Don't share credentials via email/chat

---

## 📊 API Scopes & Permissions

The service account has access to:

### Google Drive API
- **Scope:** `https://www.googleapis.com/auth/drive`
- **Purpose:** Create and manage files (Forms, Sheets, Docs)

### Google Docs API
- **Scope:** `https://www.googleapis.com/auth/documents`
- **Purpose:** Create and edit Google Docs

### Google Sheets API
- **Scope:** `https://www.googleapis.com/auth/spreadsheets`
- **Purpose:** Create and edit Google Sheets

### Google Forms API
- **Scope:** `https://www.googleapis.com/auth/forms.body`
- **Purpose:** Create Google Forms (limited functionality)

### Google Analytics Admin API
- **Scope:** `https://www.googleapis.com/auth/analytics.admin`
- **Purpose:** Track form engagement (optional)

---

## 🐛 Troubleshooting

### Issue: "Authentication failed"

**Solution:**
1. Check `.env` file exists and has correct values
2. Verify `credentials/google-service-account.json` exists
3. Check file permissions: `ls -la .env credentials/`
4. Run test script: `python tools/test_google_auth.py`

### Issue: "Permission denied" errors

**Solution:**
```bash
# Fix file permissions
chmod 600 .env
chmod 600 credentials/google-service-account.json
```

### Issue: "Module not found" errors

**Solution:**
```bash
# Install dependencies
pip install -r tools/requirements.txt
```

### Issue: "Insufficient permissions" API error

**Solution:**
- Check that service account has the required API scopes
- Enable APIs in Google Cloud Console:
  - Google Drive API
  - Google Docs API
  - Google Sheets API
  - Google Forms API

---

## 📚 Additional Resources

### Google Cloud Documentation
- [Service Accounts](https://cloud.google.com/iam/docs/service-accounts)
- [Google Workspace APIs](https://developers.google.com/workspace)
- [Python Client Library](https://github.com/googleapis/google-api-python-client)

### API References
- [Google Drive API](https://developers.google.com/drive/api/v3/reference)
- [Google Docs API](https://developers.google.com/docs/api/reference/rest)
- [Google Sheets API](https://developers.google.com/sheets/api/reference/rest)
- [Google Forms API](https://developers.google.com/forms/api/reference/rest)

### Thesis-Specific Guides
- [Zotero Setup](../bibliography/zotero_setup_guide.md)
- [Weekly Logs](../progress/weekly_logs/TEMPLATE_weekly_log.md)
- [Research Plans](../README.md#research-themes)

---

## 🔄 Workflow Examples

### Example 1: Create and Deploy Questionnaire

```bash
# 1. Create Google Form
python tools/create_google_form.py --theme 1

# 2. Add questions manually via web interface
# (Use template provided in script output)

# 3. Share form link with participants
# (Export responses to CSV when complete)

# 4. Export responses to Sheets for analysis
python tools/export_to_sheets.py \
  --file tema1_transformare_procese/04_data_collection/survey_responses.csv \
  --title "Survey Results - Tema 1"
```

### Example 2: Share Chapter with Supervisor

```bash
# 1. Write chapter in Markdown
# tema1_transformare_procese/03_writing/chapter2_literature.md

# 2. Publish to Google Docs
python tools/publish_to_docs.py \
  --file tema1_transformare_procese/03_writing/chapter2_literature.md \
  --title "Capitol 2: Revizia Literaturii - Tema 1"

# 3. Open URL from output
# 4. Share with supervisor (Commenter access)
# 5. Collect feedback
# 6. Update Markdown file based on comments
```

### Example 3: Data Analysis Pipeline

```bash
# 1. Export raw data to Sheets
python tools/export_to_sheets.py \
  --file raw_data.csv \
  --title "Raw Survey Data"

# 2. Analyze in SPSS/Python (locally)

# 3. Export results to Sheets
python tools/export_to_sheets.py \
  --file analysis_results.xlsx \
  --title "Analysis Results"

# 4. Share with supervisor for review
```

---

## 📝 Notes

- **Google Forms API Limitations:** Full form creation via API is limited. Use the web interface to add questions after creating the form.
- **Service Account Limitations:** Service accounts create files that are owned by the service account, not by you. You'll need to share files with yourself if you want to access them via your personal Google account.
- **Quota Limits:** Google APIs have usage quotas. For thesis work, you're unlikely to hit limits, but be aware of them.
- **Data Ownership:** All files created via the service account belong to the GCP project. Export important files locally as backups.

---

## ✅ Checklist

Before using Google Cloud tools, ensure:

- [ ] `.env` file exists with correct credentials
- [ ] `credentials/google-service-account.json` exists
- [ ] File permissions are secure (chmod 600)
- [ ] Dependencies installed (`pip install -r tools/requirements.txt`)
- [ ] Authentication test passes (`python tools/test_google_auth.py`)
- [ ] `.gitignore` excludes `.env` and `credentials/`

---

**Last Updated:** 2024-10-22
**Maintainer:** Robert Eduard Antal (robert@antal.me)
