# Google Drive Storage Solutions

**Issue:** Service account has exceeded storage quota
**Error:** "The user's Drive storage quota has been exceeded"

You have **two options**: Clean up existing files OR add more storage space.

---

## 🆓 Option A: Clean Up Storage (Free, Fast)

### Method 1: Automated Cleanup Script (Recommended)

I've created a script to help you manage the service account's Drive storage.

#### Step 1: Check Storage Status

```bash
cd /home/antal/projects/licentafspac
python tools/cleanup_drive_storage.py --info
```

**Output:**
```
📊 Storage Information
User: fspac-study-tools@fspac-2025-study-tools.iam.gserviceaccount.com
Total Quota: 15.00 GB
Used: 15.05 GB (100.3%)
⚠️  QUOTA EXCEEDED! Delete files to free up space.
```

#### Step 2: List All Files

```bash
python tools/cleanup_drive_storage.py --list --show-size
```

**Output:**
```
Found 47 file(s):

1. Old Campaign Report Q2
   ID: 1abc...xyz
   Type: spreadsheet
   Size: 2.45 MB
   Created: 2024-08-15, Modified: 2024-09-01

2. Test Document
   ID: 2def...xyz
   Type: document
   Size: 156.78 KB
   Created: 2024-09-20, Modified: 2024-10-01

...
```

#### Step 3: Delete Files

**Option 3A: Delete specific files**
```bash
# Delete by file ID (from list above)
python tools/cleanup_drive_storage.py --delete 1abc...xyz
python tools/cleanup_drive_storage.py --delete 2def...xyz
```

**Option 3B: Delete ALL files (CAREFUL!)**
```bash
# This will ask for confirmation
python tools/cleanup_drive_storage.py --delete-all
```

Type `DELETE ALL` to confirm deletion.

#### Step 4: Verify Storage Freed

```bash
python tools/cleanup_drive_storage.py --info
```

**Expected:**
```
📊 Storage Information
Used: 2.34 GB (15.6%)
Remaining: 12.66 GB
✅ Storage quota OK!
```

#### Step 5: Test Publishing

Once storage is freed, try publishing again:

```bash
python tools/publish_via_drive.py \
  --file PROJECT_OVERVIEW.md \
  --email robert@antal.me \
  --title "Thesis Overview"
```

---

### Method 2: Manual Cleanup via Web Interface

If you prefer to use the web interface:

#### Step 1: Access Drive as Service Account

**Problem:** Service accounts don't have a password, so you can't log in directly.

**Workaround:** Share files with your personal account first, then manage from there.

Run this script to list and share files:
```bash
# This would require a custom script - see Automated method above
```

**OR** use the automated script (Method 1) which is much easier.

---

## 💰 Option B: Add More Storage (Paid)

Service accounts use the **Google Workspace** storage pool. To add storage:

### Step 1: Check Your Google Cloud Billing

1. Go to: https://console.cloud.google.com/billing
2. Select project: `fspac-2025-study-tools`
3. Check if billing is enabled

### Step 2: Understand Storage Options

**Google Workspace Storage:**
- Service accounts share storage with the Google Workspace organization
- If this is a personal project (not a company Workspace), you have 15 GB free

**Options to Add Storage:**

**A. Google One (Personal)** - NOT compatible with service accounts
- This won't work because service accounts are separate from personal Google accounts

**B. Google Workspace Subscription** - ~$6-12/month
- Requires setting up a Google Workspace organization
- Basic: $6/user/month (30 GB per user)
- Business Standard: $12/user/month (2 TB per user)
- Visit: https://workspace.google.com/pricing

**C. Google Cloud Storage** - Alternative approach
- Instead of Google Drive, use Cloud Storage buckets
- Much cheaper: $0.020/GB/month (~$0.30/month for 15 GB)
- Requires code changes (use Cloud Storage API instead of Drive API)

### Step 3: For Thesis Work (Recommendation)

**Best Option:** Clean up storage (Option A)

**Why:**
- Free
- Fast (5 minutes)
- Service accounts typically accumulate test files
- Thesis documents are small (a few MB each)
- 15 GB free quota is plenty for thesis work

**Cost Analysis:**
- Thesis documents: ~50 MB total (all chapters, drafts)
- Survey data: ~10 MB (CSV files)
- Total needed: ~100 MB
- Free quota: 15 GB = 15,000 MB

**Conclusion:** You have 150x more space than needed if you clean up old files!

---

## 🎯 Recommended Solution

For your thesis project, **clean up storage** is the best option:

### Quick Cleanup (5 minutes)

```bash
# 1. Check what's using space
python tools/cleanup_drive_storage.py --list --show-size

# 2. Delete old/test files
python tools/cleanup_drive_storage.py --delete-all

# 3. Verify storage freed
python tools/cleanup_drive_storage.py --info

# 4. Test publishing
python tools/publish_via_drive.py \
  --file PROJECT_OVERVIEW.md \
  --email robert@antal.me
```

**Expected Results:**
- ✅ 10-15 GB freed up
- ✅ Plenty of space for thesis documents
- ✅ $0 cost
- ✅ 5 minutes of work

---

## 🔄 Alternative: Use Your Personal Google Account

If cleanup doesn't work or you prefer not to use the service account:

### Option C: Personal Google Drive

**Advantages:**
- 15 GB free storage (separate from service account)
- Easy web interface
- No service account complexity

**How:**

1. **Upload manually to your Google Drive:**
   - Go to https://drive.google.com
   - Upload `PROJECT_OVERVIEW.md`
   - Google will convert to Google Docs
   - Share with yourself

2. **Use Google Drive desktop app:**
   - Install Google Drive for Desktop
   - Drag files to `~/Google Drive/` folder
   - Auto-syncs to your account

3. **Create Google Docs directly:**
   - Go to https://docs.google.com
   - Create new document
   - Copy-paste content from `PROJECT_OVERVIEW.md`
   - Format as needed

**For Automation:**
You can still use OAuth2 (user authentication) instead of service accounts for the Python scripts. This requires a different credential setup but gives you access to your personal Drive.

---

## 📊 Storage Usage Breakdown

**Typical Thesis Files:**
- Overview document: 50 KB
- Chapter drafts (5-6 chapters): ~500 KB total
- Survey data (CSV): 100-500 KB
- Interview transcripts: 1-5 MB
- Final thesis PDF: 2-5 MB
- Presentation slides: 5-10 MB

**Total:** ~20-30 MB for entire thesis

**Free Quota:** 15 GB = 15,000 MB

**Conclusion:** You need less than 0.2% of available storage!

---

## ✅ Next Steps

**Recommended Path:**

```bash
# 1. Clean up service account storage (do this now)
cd /home/antal/projects/licentafspac
python tools/cleanup_drive_storage.py --delete-all

# 2. Test publishing
python tools/publish_via_drive.py \
  --file PROJECT_OVERVIEW.md \
  --email robert@antal.me \
  --title "Thesis Overview"

# 3. If successful, you're done!
# If still issues, switch to personal Google account (Option C)
```

---

## 🆘 Troubleshooting

### Issue: "Permission denied" when running cleanup script

**Fix:**
```bash
chmod +x tools/cleanup_drive_storage.py
python tools/cleanup_drive_storage.py --info
```

### Issue: "Service account has no files but quota still exceeded"

**Reason:** Files might be in trash or shared drives

**Fix:**
1. Empty trash via API (add to script)
2. Check shared drives
3. Wait 24 hours for quota to update

### Issue: Cleanup doesn't free enough space

**Options:**
1. Use your personal Google account (Option C)
2. Switch to Google Cloud Storage buckets
3. Upgrade to Google Workspace (if needed for large datasets)

---

## 📝 Summary

| Solution | Cost | Time | Recommended For |
|----------|------|------|-----------------|
| **Clean up storage** | Free | 5 min | ✅ Most users |
| Add Google Workspace | $6-12/mo | 30 min | Large organizations |
| Use personal account | Free | 10 min | If cleanup fails |
| Cloud Storage buckets | ~$0.30/mo | 2 hours | Large file storage |

**For thesis work:** Clean up storage (free, fast, sufficient)

---

**Last Updated:** 2024-10-22
**Related:** See `docs/GOOGLE_CLOUD_SETUP.md` for API setup
