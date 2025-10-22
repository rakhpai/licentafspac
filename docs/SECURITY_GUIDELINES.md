# Security & Data Protection Guidelines

**Project:** Lucrare de Licență - AI în Agențiile de Publicitate
**Student:** Robert Eduard Antal
**Date:** 2024-10-22

---

## 🔐 Overview

This project handles **sensitive data** that must be protected:

1. **Personal Data (GDPR-protected)**
   - Interview recordings and transcriptions
   - Participant contact information
   - Survey responses with identifying information

2. **Confidential Business Data**
   - Campaign performance metrics
   - Agency client information
   - Internal strategy documents

3. **Credentials & API Keys**
   - Google Cloud service account credentials
   - OpenAI/Claude API keys
   - Database connection strings

**Legal Framework:** GDPR (General Data Protection Regulation)
**University Requirements:** Data protection and ethical research standards

---

## 🛡️ Data Classification

### 🔴 NEVER COMMIT TO GIT (High Risk)

These files are **excluded by .gitignore**:

```
# Sensitive Personal Data
**/04_data_collection/interviews_transcribed/
**/04_data_collection/audio_recordings/
**/04_data_collection/consent_forms_signed/
participants_list*
contact_info*

# Confidential Business Data
**/04_data_collection/campaign_data/
**/04_data_collection/performance_metrics/
*_campaigns.csv
*_data.xlsx

# Individual Survey Responses (GDPR)
*_responses.csv
*_responses.xlsx
*.sav  # SPSS raw data files
questionnaire_raw_data*

# Credentials & Secrets
.env
credentials.json
api_keys.txt
passwords.txt
credentials/

# Legal Documents (with signatures)
**/nda_signed/
**/contracts/
```

### 🟡 COMMIT WITH CAUTION (Medium Risk)

These files CAN be committed but must be **reviewed carefully**:

```
# Anonymized/Aggregated Data (safe if properly anonymized)
**/aggregated_results.csv
**/anonymous_summary.xlsx

# Analysis Scripts (safe if no hardcoded credentials)
**/*.R
**/*.py
**/*.syntax  # SPSS syntax

# Codebooks & Frameworks (safe)
**/codebook_*.xlsx
**/coding_framework_*.md
```

**Before committing:**
1. Remove all personally identifiable information (PII)
2. Check for hardcoded credentials or API keys
3. Verify data is aggregated (no individual responses)
4. Ensure compliance with NDAs from agencies

### 🟢 SAFE TO COMMIT (Low Risk)

These files are safe for version control:

```
# Documentation
*.md (except personal_thoughts.md, diary.md)
README.md
progress/*.md
docs/*.md

# Templates & Examples
TEMPLATE_*
EXAMPLE_*

# Bibliography
bibliography/*.bib
bibliography/reading_notes/*.md

# Code & Scripts (without credentials)
tools/*.py
analysis/*.R

# Configuration (without secrets)
.env.example
.gitignore
requirements.txt
```

---

## 📋 GDPR Compliance Checklist

### Before Starting Data Collection

- [ ] **Informed Consent**
  - Prepare consent forms explaining data usage
  - Get written consent from all participants
  - Store signed consent forms securely (NOT in git)

- [ ] **Data Minimization**
  - Only collect data necessary for research
  - Don't ask for unnecessary personal information

- [ ] **Purpose Limitation**
  - Clearly state that data is for academic research only
  - Don't use data for other purposes

### During Data Collection

- [ ] **Secure Storage**
  - Store raw data locally (NOT in cloud/git)
  - Use encrypted folders if possible
  - Restrict file permissions: `chmod 600`

- [ ] **Anonymization**
  - Assign participant IDs (P001, P002, etc.)
  - Replace names with IDs in transcriptions
  - Remove identifying information from datasets

- [ ] **Access Control**
  - Only you and your supervisor access raw data
  - Use service accounts (not personal accounts) for APIs
  - Don't share credentials

### After Data Collection

- [ ] **Data Retention**
  - Keep raw data only as long as necessary
  - Delete after thesis submission (or per university policy)
  - Keep anonymized/aggregated data for reproducibility

- [ ] **Participant Rights**
  - Provide data access if participants request it
  - Delete participant data if they withdraw consent
  - Inform participants of data storage duration

---

## 🔑 Credential Management

### .env File Security

**Current setup:**
```bash
# File permissions (owner read/write only)
-rw-------  1 antal antal  .env
-rw-------  1 antal antal  credentials/google-service-account.json
```

**Best practices:**
1. **Never commit** `.env` to git (.gitignore blocks it)
2. **Set secure permissions:** `chmod 600 .env`
3. **Rotate credentials** if compromised
4. **Use separate credentials** for production/testing

### API Key Safety

**✅ DO:**
- Store API keys in `.env` file
- Use environment variables in code:
  ```python
  import os
  api_key = os.getenv('OPENAI_API_KEY')
  ```
- Rotate keys periodically
- Monitor usage in provider dashboards

**❌ DON'T:**
- Hardcode API keys in scripts
- Commit API keys to git
- Share keys via email/chat
- Use production keys for testing

### Service Account Best Practices

**Google Cloud Service Account:**
- Email: `fspac-study-tools@fspac-2025-study-tools.iam.gserviceaccount.com`
- Type: Robot account (not tied to personal email)

**Advantages:**
- ✅ Doesn't require personal Google login
- ✅ Can be shared with supervisor if needed
- ✅ Limited scopes (only necessary permissions)
- ✅ Auditable (tracks all actions)

**Security:**
1. **Principle of Least Privilege**
   - Only grant necessary API scopes
   - Current scopes: Drive, Docs, Sheets, Forms (read/write)
   - No admin or delete permissions

2. **Access Monitoring**
   - Check GCP logs for unusual activity
   - Review API usage in Cloud Console

3. **Credential Rotation**
   - If credentials leaked → revoke and regenerate
   - Update `.env` with new credentials
   - Test with `python tools/test_google_auth.py`

---

## 📁 File Organization & Backup

### Local Storage Structure

```
/home/antal/projects/licentafspac/
├── .env                          # [chmod 600] - NEVER commit
├── credentials/                  # [chmod 600] - NEVER commit
│   └── google-service-account.json
├── tema1_transformare_procese/
│   └── 04_data_collection/
│       ├── interviews_transcribed/  # [LOCAL ONLY] - NEVER commit
│       ├── consent_forms_signed/    # [LOCAL ONLY] - NEVER commit
│       ├── aggregated_results.csv   # [SAFE] - Can commit
│       └── analysis_summary.xlsx    # [SAFE] - Can commit
└── docs/
    └── SECURITY_GUIDELINES.md    # [SAFE] - Can commit
```

### Backup Strategy

**Critical files to backup:**
1. Raw interview data (transcriptions, recordings)
2. Survey responses (before anonymization)
3. Analysis results
4. Thesis drafts

**Backup locations:**
1. **Primary:** Local machine (`/home/antal/projects/licentafspac/`)
2. **Backup 1:** External hard drive (encrypted)
3. **Backup 2:** University OneDrive/Google Drive (encrypted, if permitted)
4. **Version control (git):** Only anonymized data and code

**Important:**
- **Encrypt** backups containing personal data
- **Test** backups regularly (can you restore them?)
- **Delete** backups after thesis submission (per GDPR)

---

## 🚨 Incident Response

### If Credentials Are Compromised

1. **Immediate Actions:**
   ```bash
   # 1. Revoke compromised credentials in Google Cloud Console
   # 2. Generate new service account key
   # 3. Update .env file with new credentials
   # 4. Test authentication
   python tools/test_google_auth.py

   # 5. Review git history for leaked credentials
   git log --all --full-history -- .env
   git log --all --full-history -- credentials/
   ```

2. **If committed to git accidentally:**
   ```bash
   # WARNING: This rewrites git history!
   # Contact supervisor before doing this

   # Option 1: Remove file from last commit
   git rm --cached .env
   git commit --amend

   # Option 2: Remove from all history (dangerous!)
   # Use git-filter-repo or BFG Repo-Cleaner
   ```

3. **Notify:**
   - Thesis supervisor
   - Google Cloud admin (if enterprise account)
   - Data Protection Officer (if at university)

### If Personal Data Is Exposed

1. **Assess exposure:**
   - What data was exposed? (names, emails, interviews?)
   - Where was it exposed? (public GitHub, email, etc.)
   - Who had access?

2. **Immediate containment:**
   - Remove data from public location
   - Revoke access to exposed files
   - Document the incident

3. **Notify affected parties:**
   - Inform participants (if their data was exposed)
   - Notify university ethics committee
   - File data breach report (if required by GDPR)

4. **Prevent recurrence:**
   - Review `.gitignore` rules
   - Audit all files in git repository
   - Improve access controls

---

## ✅ Pre-Commit Checklist

Before running `git add` or `git commit`, check:

- [ ] No personal data in files to be committed
  ```bash
  git diff --cached  # Review changes
  ```

- [ ] No credentials or API keys
  ```bash
  grep -r "api_key" .  # Search for keys
  grep -r "password" .
  ```

- [ ] `.env` and `credentials/` not staged
  ```bash
  git status  # Should NOT show .env or credentials/
  ```

- [ ] Only anonymized/aggregated data
  ```bash
  # Check data files for participant IDs, not names
  ```

- [ ] No NDA-violating information
  ```bash
  # Check for agency client names, campaign details
  ```

If in doubt: **DON'T COMMIT**. You can always add files later, but removing them from git history is difficult.

---

## 📚 Resources

### GDPR & Data Protection
- [GDPR Official Text](https://gdpr-info.eu/)
- [ICO Guide to GDPR](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/)
- [Research Data Management](https://www.ukdataservice.ac.uk/manage-data/legal-ethical/consent-data-sharing)

### Git Security
- [GitHub Security Best Practices](https://docs.github.com/en/code-security/getting-started/best-practices-for-preventing-data-leaks-in-your-organization)
- [Removing Sensitive Data from Git](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

### Credential Management
- [Google Cloud IAM Best Practices](https://cloud.google.com/iam/docs/best-practices-service-accounts)
- [OWASP API Security](https://owasp.org/www-project-api-security/)

---

## 📝 Contact

**Questions about data protection?**
- Thesis Supervisor: [Supervisor email]
- University Ethics Committee: [Ethics contact]
- Data Protection Officer: [DPO contact]

**Technical issues?**
- Student: Robert Eduard Antal (robert@antal.me)

---

**Last Updated:** 2024-10-22
**Review Date:** Every month during thesis work
