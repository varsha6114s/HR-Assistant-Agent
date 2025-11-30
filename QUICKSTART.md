# Quick Start Guide - HR Assistant Agent

## Quick Setup (3 Steps)

### Step 1: Run Setup Script
```bash
cd hr_assistant_agent
./setup.sh
```

This will:
- Create a virtual environment
- Install all dependencies
- Set up the project

### Step 2: Add Your OpenAI API Key
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

Get your API key from: https://platform.openai.com/api-keys

Your `.env` file should look like:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### Step 3: Run the Application
```bash
./run.sh
```

The app will open in your browser at `http://localhost:8501`

---

## Testing the Agent

Once the app is running, try these questions:

1. **Leave Policies**
   - "How many sick leaves do I have?"
   - "What is the maternity leave policy?"
   - "Can I carry forward my annual leave?"

2. **Benefits**
   - "What health insurance benefits do we get?"
   - "Tell me about the provident fund"
   - "What is the performance bonus?"

3. **Holidays**
   - "When are the company holidays in 2024?"
   - "How many optional holidays can I take?"

4. **Working Hours**
   - "What are the flexible working hours?"
   - "Can I work from home?"

---

## Troubleshooting

### Issue: "No space left on device"
**Solution**: Free up disk space and run `./setup.sh` again

### Issue: "OPENAI_API_KEY not found"
**Solution**: Make sure you created the `.env` file with your API key

### Issue: "Module not found"
**Solution**: Run `./setup.sh` again to install dependencies

### Issue: "Port 8501 already in use"
**Solution**: 
```bash
# Kill the existing process
lsof -ti:8501 | xargs kill -9
# Then run again
./run.sh
```

---

## Manual Setup (Alternative)

If the scripts don't work, you can set up manually:

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env
# Edit .env and add your API key

# 5. Run the app
streamlit run app.py
```

---

## For Submission

### Deploy to Streamlit Cloud (Free)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "HR Assistant Agent for Rooman Challenge"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Connect your GitHub repository
   - Select `app.py` as the main file
   - Add `OPENAI_API_KEY` in the Secrets section:
     ```toml
     OPENAI_API_KEY = "sk-your-api-key-here"
     ```
   - Click "Deploy"

3. **Get Your Demo Link**
   - You'll get a URL like: `https://your-app.streamlit.app`
   - Use this as your "Working Demo Link" in the submission

---

## Creating Demo Video

### Option 1: Screen Recording (Mac)
```bash
# Press Cmd + Shift + 5
# Select "Record Selected Portion"
# Record your demo
# Save as MP4
```

### Option 2: Using OBS Studio
1. Download OBS Studio (free)
2. Set up screen capture
3. Record your demo following `DEMO_SCRIPT.md`
4. Export as MP4

### Demo Script
Follow the script in `DEMO_SCRIPT.md` for a professional 2-3 minute demo.

---

## Submission Checklist

Before submitting, make sure you have:

- Working demo link (Streamlit Cloud URL or video)
- GitHub repository (public or shared)
- All code files committed
- README.md with setup instructions
- Architecture diagram included
- .env.example file (NOT .env with real API key!)
- Demo video (optional but recommended)
- Filled the submission form: https://forms.office.com/r/GQmPNZ6PgG

---

## For the Jury Presentation

### Key Points to Mention

1. **Problem**: Employees waste time searching HR docs, HR teams get repetitive questions
2. **Solution**: AI agent with RAG architecture for instant, accurate answers
3. **Tech Stack**: 
   - OpenAI GPT-3.5 for natural language
   - LangChain for RAG pipeline
   - FAISS for vector search
   - Streamlit for beautiful UI
4. **Impact**: 70%+ reduction in HR team workload, 24/7 availability

### Demo Flow
1. Show the UI (30 sec)
2. Explain architecture (40 sec)
3. Live demo with 3 questions (60 sec)
4. Highlight features (20 sec)
5. Discuss improvements (10 sec)

---

## Tips for Success

1. **Test thoroughly** before submitting
2. **Practice your demo** multiple times
3. **Have backup screenshots** in case of technical issues
4. **Know your architecture** - be ready to explain RAG
5. **Be confident** - you built something impressive!

---

**Good luck with your submission!**

*Deadline: 29 Nov 6 PM*
