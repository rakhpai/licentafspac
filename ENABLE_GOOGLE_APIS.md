# Enable Google Cloud APIs

**Issue:** Google Drive API and Google Docs API need to be enabled for your project.

---

## 🔧 Quick Fix (5 minutes)

### Step 1: Access Google Cloud Console

Visit: https://console.cloud.google.com/

**Login with:** The Google account that owns the service account
- Service Account: `fspac-study-tools@fspac-2025-study-tools.iam.gserviceaccount.com`
- Project: `fspac-2025-study-tools`

### Step 2: Select Your Project

1. Click the project dropdown at the top of the page
2. Select: **fspac-2025-study-tools**

### Step 3: Enable APIs

**Option A: Direct Links (Fastest)**

Click these links to enable the APIs directly:

1. **Google Drive API:**
   https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=920983249571

   - Click **"ENABLE"**
   - Wait 30-60 seconds for activation

2. **Google Docs API:**
   https://console.developers.google.com/apis/api/docs.googleapis.com/overview?project=920983249571

   - Click **"ENABLE"**
   - Wait 30-60 seconds for activation

**Option B: Manual Navigation**

1. In Cloud Console, go to: **APIs & Services > Library**
2. Search for: **Google Drive API**
   - Click on it
   - Click **"ENABLE"**
3. Search for: **Google Docs API**
   - Click on it
   - Click **"ENABLE"**

### Step 4: Verify Activation

After enabling (wait 2-3 minutes), test the setup:

```bash
cd /home/antal/projects/licentafspac
python tools/test_google_auth.py
```

Expected output:
```
✅ SUCCESS: Google Cloud is properly configured!
```

### Step 5: Publish the Overview

Once APIs are enabled, publish and share the overview:

```bash
python tools/publish_and_share.py \
  --file PROJECT_OVERVIEW.md \
  --email robert@antal.me \
  --title "Lucrare de Licență: AI în Agențiile de Publicitate - Overview" \
  --role writer
```

This will:
- ✅ Create a Google Doc with the full overview
- ✅ Share it with robert@antal.me (with edit access)
- ✅ Send you an email notification with the link

---

## 📄 Alternative: View Overview Locally

If you want to view the overview right now (without waiting for API activation):

### Option 1: Read Markdown File

```bash
# Simple view in terminal
less PROJECT_OVERVIEW.md

# Or open in your text editor
code PROJECT_OVERVIEW.md
# or
nano PROJECT_OVERVIEW.md
```

### Option 2: View on GitHub

The overview is committed to your repository:

```bash
# Push to GitHub
git push origin master

# Then visit:
# https://github.com/rakhpai/licentafspac/blob/master/PROJECT_OVERVIEW.md
```

GitHub will render the Markdown beautifully with table of contents.

### Option 3: Convert to HTML/PDF

Install pandoc and convert:

```bash
# Install pandoc (if not already installed)
sudo apt-get install pandoc

# Convert to HTML
pandoc PROJECT_OVERVIEW.md -o PROJECT_OVERVIEW.html --standalone

# Convert to PDF (requires LaTeX)
pandoc PROJECT_OVERVIEW.md -o PROJECT_OVERVIEW.pdf

# Open HTML in browser
xdg-open PROJECT_OVERVIEW.html
```

---

## ✅ Summary

**What happened:**
- Google Drive API and Docs API weren't enabled for the `fspac-2025-study-tools` project
- The service account credentials are valid, but APIs need activation

**What to do:**
1. Enable Google Drive API (1 click)
2. Enable Google Docs API (1 click)
3. Wait 2-3 minutes
4. Run: `python tools/publish_and_share.py --file PROJECT_OVERVIEW.md --email robert@antal.me`

**Total time:** ~5 minutes

---

## 📧 Already Available

The **PROJECT_OVERVIEW.md** file is already created and committed to git. You can:

- Read it locally: `less PROJECT_OVERVIEW.md`
- Push to GitHub: `git push` (then view on GitHub)
- Email it to yourself: Attach the file to an email

Once you enable the APIs, the automation tools will work perfectly for future documents.

---

**Need help?** Check `docs/GOOGLE_CLOUD_SETUP.md` for full documentation.
