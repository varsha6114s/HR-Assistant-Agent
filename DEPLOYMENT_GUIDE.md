# Streamlit Deployment Guide

## Step-by-Step Deployment to Streamlit Cloud

### Step 1: Verify Your GitHub Repository

Your repository is already at: https://github.com/varsha6114s/HR-Assistant-Agent

Make sure:
- ✅ Code is pushed to GitHub
- ✅ Repository is public (or you have access)
- ✅ `app.py` is in the root directory
- ✅ `requirements.txt` exists

### Step 2: Go to Streamlit Cloud

1. Visit: https://share.streamlit.io
2. Click **"Sign in"** (use your GitHub account)
3. Authorize Streamlit to access your GitHub

### Step 3: Deploy New App

1. Click **"New app"** button
2. Fill in the details:
   - **Repository**: `varsha6114s/HR-Assistant-Agent`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL** (optional): Choose a custom name like `hr-assistant-agent`

3. Click **"Deploy!"**

### Step 4: Wait for Deployment

- Streamlit will install dependencies from `requirements.txt`
- This takes 2-5 minutes
- You'll see logs showing the installation progress

### Step 5: Access Your App

Once deployed, you'll get a URL like:
- `https://hr-assistant-agent.streamlit.app`
- Or `https://varsha6114s-hr-assistant-agent.streamlit.app`

## Troubleshooting

### Issue: "Repository not found"
**Solution**: 
- Make sure repository is public
- Re-authorize Streamlit's GitHub access
- Check repository name spelling

### Issue: "Module not found" during deployment
**Solution**: 
- Check `requirements.txt` has all dependencies
- Make sure package names are correct
- Try deploying again (sometimes transient errors)

### Issue: "App keeps restarting"
**Solution**:
- Check the logs in Streamlit Cloud dashboard
- Look for Python errors
- Make sure all imports are correct

### Issue: Can't sign in to Streamlit Cloud
**Solution**:
- Use GitHub account to sign in
- Clear browser cache and try again
- Try incognito/private browsing mode

## Alternative: Local Demo Video

If Streamlit Cloud deployment doesn't work, you can:

1. **Record a video** of your local app running
2. **Upload to YouTube** (unlisted)
3. **Use YouTube link** as your demo link

### How to Record:

**On Mac:**
```bash
# Press Cmd + Shift + 5
# Select "Record Selected Portion"
# Record your demo
# Save as MP4
```

**On Windows:**
```bash
# Press Windows + G
# Click Record button
# Record your demo
```

## What to Submit

For Rooman Challenge, you need:

1. **GitHub Repository**: https://github.com/varsha6114s/HR-Assistant-Agent ✅
2. **Demo Link**: Either:
   - Streamlit Cloud URL (e.g., `https://your-app.streamlit.app`)
   - OR YouTube video link
   - OR Local demo video file

## Need Help?

Tell me specifically what error you're seeing:
- Screenshot of the error
- Error message text
- Which step you're stuck on

I'll help you fix it!
