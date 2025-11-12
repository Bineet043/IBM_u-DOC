# Streamlit Cloud Deployment Guide for U-DOC

## Issue: Clone Failed Error
If you see: "Failed to download the sources for repository"

### Step 1: Verify Repository Settings
1. Go to https://github.com/Bineet043/IBM_u-DOC
2. Click **Settings** (gear icon at top right)
3. Under **Access**, ensure the repo is **Public** (not Private)
   - If Private: click "Change to public" and confirm
4. Click **Branches** (left sidebar)
5. Ensure `main` branch exists and has no protection rules that block Streamlit

### Step 2: Check for Large Files
1. Go to the repo homepage
2. Look at file sizes — the PowerPoint file might be too large
3. **Optional:** Remove the `.pptx` file if it's causing issues:
   ```powershell
   cd C:/Users/VICTUS/IBM
   git rm "U-DOC-AI-Powered-Clinical-Document-Intelligence (1).pptx"
   git commit -m "Remove large PowerPoint file to fix Streamlit deployment"
   git push origin main
   ```

### Step 3: Retry Streamlit Deployment
1. Go to https://share.streamlit.io
2. Click **Create app**
3. Fill in:
   - **GitHub repo:** `Bineet043/IBM_u-DOC`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **Deploy**

### Step 4: Add API Key to Secrets (After Deployment)
1. Once the app is deployed, click the **three dots** (⋯) in top-right corner
2. Select **Settings**
3. Click **Secrets**
4. Paste this (replace with your actual key):
   ```
   GOOGLE_API_KEY = "AIzaSyBD-Rdc-igMlhYOLNTqUso5ox4uYrp_1Jo"
   ```
5. Click **Save** — app will redeploy automatically

## Troubleshooting Checklist
- [ ] Repository is **Public**
- [ ] Branch `main` exists and is up-to-date
- [ ] `app.py` exists in root directory
- [ ] `requirements.txt` exists in root directory
- [ ] `.env` file is in `.gitignore` (not committed)
- [ ] No merge conflicts in git history
- [ ] API key is set in Streamlit Secrets

## Local Testing Before Deploy
To test locally, ensure you have:
```powershell
# 1. Activate venv
& .venv\Scripts\Activate.ps1

# 2. Run the app
streamlit run app.py

# 3. Open browser to http://localhost:8501
```

If the app works locally but fails on Streamlit Cloud, the issue is usually:
- API key not in secrets (403 error)
- Repository access issue (clone error)
- Dependency version mismatch

## Need Help?
- Streamlit Docs: https://docs.streamlit.io/
- Streamlit Community: https://discuss.streamlit.io/
