# Thesis Automation Tools

Tools pentru automatizarea task-urilor tezei de licență.

---

## 📝 Publishing & Documentation

### `publish_markdown_formatted.py` ⭐ RECOMANDAT
Convertește Markdown în Google Docs cu formatare completă.

**Caracteristici:**
- ✅ Headings (H1-H6) formatate corect
- ✅ Liste (bullet și numerotate)
- ✅ Bold, italic, links
- ✅ Creare directă în Shared Drive (bypass quota)

**Usage:**
```bash
python publish_markdown_formatted.py \
  --file chapter1.md \
  --title "Capitol 1" \
  --folder-id 0APsOGraGUhOQUk9PVA \
  --share robert@antal.me
```

### `publish_markdown_to_docs.py`
Folosește biblioteca markgdoc (DEPRECATED - vezi eroarea de quota).

### `publish_to_docs.py`
Upload simplu fără formatare (text plain).

### `publish_via_drive.py`
Upload prin Drive API.

### `publish_and_share.py`
Upload și share combinat.

---

## 🗂️ Storage Management

### `check_drive_quota.py`
Verifică quota și fișiere în Drive.

```bash
python check_drive_quota.py
```

### `cleanup_drive_storage.py`
Gestionare interactivă fișiere (listare, ștergere).

```bash
python cleanup_drive_storage.py --list
python cleanup_drive_storage.py --delete FILE_ID
python cleanup_drive_storage.py --delete-all
```

### `force_cleanup.py`
Ștergere batch fără confirmare.

```bash
python force_cleanup.py
```

---

## 📊 Data Export

### `export_to_sheets.py`
Export CSV/Excel în Google Sheets.

```bash
python export_to_sheets.py \
  --file data.csv \
  --title "Survey Results"
```

---

## 📋 Forms & Surveys

### `create_google_form.py`
Creează chestionare pentru temele tezei.

```bash
python create_google_form.py --theme 1  # Transformarea proceselor
python create_google_form.py --theme 2  # Competențe
python create_google_form.py --theme 3  # ROI metrici
```

---

## 🔧 Utilities

### `test_google_auth.py`
Testează autentificarea Google Cloud.

```bash
python test_google_auth.py
```

### `share_document.py`
Share document cu email.

```bash
python share_document.py DOC_ID email@example.com writer
```

### `upload_to_shared_folder.py`
Upload în Shared Drive.

```bash
python upload_to_shared_folder.py FILE FOLDER_ID "Title"
```

### `check_project_org.py`
Verifică linkare project la organizație.

```bash
python check_project_org.py
```

---

## 📦 Installation

```bash
# Install all dependencies
cd /home/antal/projects/licentafspac
pip install -r tools/requirements.txt
```

**Dependencies:**
- google-api-python-client
- google-auth
- google-auth-httplib2
- google-auth-oauthlib
- python-dotenv
- pandas, openpyxl
- markgdoc

---

## 🔑 Setup

1. **Environment variables:**
   - Ensure `.env` file exists in project root
   - Contains `GOOGLE_APPLICATION_CREDENTIALS` path

2. **Credentials:**
   - Service account JSON in `credentials/google-service-account.json`
   - chmod 600 permissions

3. **Shared Drive:**
   - Create Shared Drive in Google Drive
   - Share with service account email
   - Use Shared Drive ID in commands

---

## 🎯 Common Workflows

### Publish thesis chapter
```bash
python tools/publish_markdown_formatted.py \
  --file chapter1.md \
  --title "Capitol 1: Introducere" \
  --folder-id 0APsOGraGUhOQUk9PVA \
  --share supervisor@univ.ro \
  --role commenter
```

### Export survey data
```bash
python tools/export_to_sheets.py \
  --file survey_responses.csv \
  --title "Survey Results - Tema 1"
```

### Clean up old files
```bash
python tools/cleanup_drive_storage.py --list
python tools/cleanup_drive_storage.py --delete-all
```

---

## 📚 Documentation

Full documentation: `docs/GOOGLE_CLOUD_SETUP.md`

---

**Last Updated:** 2024-10-22
**Author:** Robert Eduard Antal
