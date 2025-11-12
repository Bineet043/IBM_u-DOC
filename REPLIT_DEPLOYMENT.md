# Deploy U-DOC on Replit

## Step 1: Go to Replit
1. Visit https://replit.com
2. Sign up or log in with GitHub (recommended)

## Step 2: Create a New Replit Project
1. Click **"Create Replit"** (top-left)
2. Choose **"Import from GitHub"**
3. Paste: `https://github.com/Bineet043/IBM_u-DOC.git`
4. Click **"Import"** — Replit will clone your repo

## Step 3: Wait for Setup
- Replit will automatically:
  - Read `replit.nix` (installs Python)
  - Read `.replit` (sets up run command)
  - Install dependencies from `requirements.txt`
  - Start the Streamlit server

## Step 4: Add API Key to Replit Secrets
1. Click **"Secrets"** (lock icon in left sidebar)
2. Add a new secret:
   - **Key:** `GOOGLE_API_KEY`
   - **Value:** `AIzaSyBD-Rdc-igMlhYOLNTqUso5ox4uYrp_1Jo`
3. Click **"Add Secret"**

## Step 5: Run the App
1. Click the **"Run"** button (top)
2. The Streamlit app will start on Replit's domain
3. You'll see a URL like: `https://ibm-u-doc.replit.dev`

## Step 6: Share Your App
- Copy the URL and share it with anyone
- It will be publicly accessible
- You can also set it to private in settings if needed

## Troubleshooting
- **Port issues:** Replit uses port 3000 by default (configured in `.replit`)
- **Dependencies failing:** Check the console — sometimes PyMuPDF needs extra build tools (handled by `replit.nix`)
- **App not starting:** Click **"Run"** again or refresh the browser

## Accessing Replit Secrets in Your App
Your `app.py` already handles this:
```python
try:
    api_key = st.secrets.get("GOOGLE_API_KEY")
except:
    api_key = os.getenv('GOOGLE_API_KEY')
```

Replit automatically exposes secrets as environment variables, so both methods work!

## Keep Your Replit App Alive
By default, Replit puts the app to sleep after 1 hour of inactivity. To keep it running 24/7:
1. Go to https://replit.com/account
2. Look for **"Always On"** plan (paid option)
3. Or simply ping the URL every hour using a free uptime monitor like:
   - https://uptimerobot.com (free tier)
   - https://www.better-uptime.com (free tier)

---

**Your app should be live in 2-3 minutes!** 🚀
