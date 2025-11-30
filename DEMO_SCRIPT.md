# Demo Script for HR Assistant Agent

## 2-3 Minute Video Demo Script

### Introduction (30 seconds)
"Hello! I'm presenting the HR Assistant Agent - an AI-powered solution that helps employees instantly get answers to HR queries about policies, benefits, and leave."

**Show**: Landing page of the application

### Problem Statement (20 seconds)
"Employees often waste time searching through multiple HR documents, and HR teams get overwhelmed with repetitive questions. Our agent solves this using AI."

**Show**: Sidebar with statistics and example questions

### Architecture Overview (40 seconds)
"The system uses a RAG (Retrieval Augmented Generation) architecture:
1. HR documents are processed and stored in FAISS vector database
2. When a user asks a question, relevant context is retrieved
3. OpenAI GPT-3.5 generates accurate answers based on this context
4. Built with LangChain for the RAG pipeline and Streamlit for the UI"

**Show**: Architecture diagram (assets/architecture_diagram.png)

### Live Demo (60 seconds)

**Query 1**: "How many sick leaves do I have?"
- Type the question
- Click "Ask Question"
- Show the instant, accurate response

**Query 2**: "What is the maternity leave policy?"
- Demonstrate another query
- Highlight the detailed, policy-based answer

**Query 3**: "When are the company holidays?"
- Show how it handles different query types
- Point out the comprehensive list in the response

**Show**: 
- Chat history building up
- Statistics updating
- Smooth UI interactions

### Key Features (20 seconds)
"Key features include:
- Natural language understanding
- Conversation memory for follow-ups
- Beautiful, modern UI with dark theme
- Sub-2-second response time
- 24/7 availability"

**Show**: Example questions in sidebar, clear history button

### Conclusion (10 seconds)
"This agent can reduce HR team workload by 70%+ while providing employees instant, accurate answers. Thank you!"

**Show**: Final view of the application

---

## Presentation Tips

### For Live Demo
1. **Prepare Environment**
   - Have the app running before starting
   - Clear any previous chat history
   - Have the architecture diagram ready

2. **Smooth Flow**
   - Practice the questions beforehand
   - Ensure stable internet for API calls
   - Have backup screenshots if API fails

3. **Highlight Technical Aspects**
   - Mention RAG architecture
   - Explain vector database usage
   - Emphasize LangChain integration
   - Show the tech stack

4. **Show Business Value**
   - Time savings for employees
   - Reduced HR team workload
   - 24/7 availability
   - Scalability

### Questions You Might Face

**Q: Why did you choose this agent?**
A: HR queries are common, relatable, and demonstrate RAG architecture well. The problem is clear and the solution is measurable.

**Q: How does RAG work?**
A: Documents are split into chunks and embedded into vectors. When queried, similar chunks are retrieved and passed to the LLM as context for accurate answers.

**Q: What if the answer isn't in the documents?**
A: The agent is instructed to state when information isn't available and suggest contacting HR directly.

**Q: How would you scale this?**
A: Use managed vector databases (Pinecone), implement caching, add load balancing, and consider fine-tuning for better performance.

**Q: What about data privacy?**
A: All processing can be done on-premises. For production, we'd use private LLM deployments or ensure data encryption.

**Q: How do you handle document updates?**
A: Currently manual rebuild. Future: automated pipeline that detects changes and updates the vector store incrementally.

---

## Key Points to Emphasize

### Technical Excellence
- Industry-standard RAG architecture
- Proper use of LangChain framework
- Vector database for semantic search
- Conversation memory for context
- Clean, modular code structure

### Business Impact
- Solves real HR pain point
- Measurable time savings
- Reduces repetitive work
- Improves employee experience
- Available 24/7

### Implementation Quality
- Beautiful, professional UI
- Comprehensive documentation
- Easy setup and deployment
- Scalable architecture
- Production-ready code

---

## Demo Queries (Backup List)

### Leave Policies
- "How many sick leaves do I have?"
- "What is the maternity leave policy?"
- "Can I carry forward my annual leave?"
- "What is the notice period for resignation?"

### Benefits
- "What health insurance benefits do we get?"
- "Tell me about the provident fund"
- "What is the performance bonus structure?"
- "Do we have gym membership reimbursement?"

### Working Hours
- "What are the flexible working hours?"
- "Can I work from home?"
- "What are the core hours?"

### Holidays
- "When are the company holidays in 2024?"
- "How many optional holidays can I take?"

### General
- "What is the dress code?"
- "How do I apply for leave?"
- "What training benefits are available?"

---

## Screen Recording Tips

### Setup
1. Close unnecessary applications
2. Clear browser cache and history
3. Set browser zoom to 100%
4. Use full-screen mode for recording
5. Test audio before recording

### Recording
1. Use tools like OBS Studio, Loom, or QuickTime
2. Record at 1080p resolution
3. Enable cursor highlighting
4. Speak clearly and at moderate pace
5. Pause briefly between sections

### Editing
1. Add intro slide with your name and project title
2. Add text overlays for key points
3. Trim any long pauses
4. Add background music (optional, keep it subtle)
5. Export in MP4 format

---

## Submission Checklist

Before submitting, ensure you have:

- Working demo link (Streamlit Cloud or local)
- GitHub repository (public or shared link)
  - Complete source code
  - All dependencies in requirements.txt
  - Sample HR documents
  - Clear README with setup instructions
- Architecture diagram (in README and assets/)
- README document with:
  - Overview and problem statement
  - Features and limitations
  - Tech stack and APIs used
  - Setup and run instructions
  - Potential improvements
- 2-3 minute video demo (optional but recommended)
- Filled submission form

---

**Good luck with your presentation!**
