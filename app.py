"""
Streamlit UI for HR Assistant Agent
Enhanced version with additional features
"""

import streamlit as st
import sys
import os
from datetime import datetime
from dotenv import load_dotenv
import time

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from hr_agent import HRAssistantAgent


# Page configuration
st.set_page_config(
    page_title="HR Assistant Agent",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful dark theme
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #6366f1;
        --secondary-color: #8b5cf6;
        --background-dark: #0f172a;
        --surface-dark: #1e293b;
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
    }
    
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        padding: 2rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3);
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .header-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-align: center;
    }
    
    .header-subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        text-align: center;
        margin-top: 0.5rem;
    }
    
    .demo-badge {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        font-size: 0.9rem;
        display: inline-block;
        margin-top: 1rem;
    }
    
    /* Chat message styling */
    .user-message {
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 1rem 1rem 0.2rem 1rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        animation: slideInRight 0.3s ease-out;
    }
    
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .assistant-message {
        background: #1e293b;
        color: #f1f5f9;
        padding: 1rem 1.5rem;
        border-radius: 1rem 1rem 1rem 0.2rem;
        margin: 1rem 0;
        border-left: 4px solid #6366f1;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        animation: slideInLeft 0.3s ease-out;
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    /* Stats cards */
    .stat-card {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        padding: 1.5rem;
        border-radius: 0.8rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        color: white;
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 0.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(99, 102, 241, 0.4);
    }
    
    /* Input styling */
    .stTextInput>div>div>input {
        background: #1e293b;
        color: #f1f5f9;
        border: 2px solid #334155;
        border-radius: 0.5rem;
        padding: 0.75rem;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #6366f1;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 1.5rem;
        border-radius: 0.8rem;
        border-left: 4px solid #6366f1;
        margin: 1rem 0;
        color: #f1f5f9;
    }
    
    /* Feature highlight */
    .feature-box {
        background: rgba(99, 102, 241, 0.1);
        border: 1px solid rgba(99, 102, 241, 0.3);
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        color: #f1f5f9;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1e293b;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #6366f1;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #8b5cf6;
    }
    
    /* Typing indicator */
    .typing-indicator {
        display: inline-block;
        padding: 1rem;
    }
    
    .typing-indicator span {
        height: 10px;
        width: 10px;
        background: #6366f1;
        border-radius: 50%;
        display: inline-block;
        margin: 0 2px;
        animation: typing 1.4s infinite;
    }
    
    .typing-indicator span:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-indicator span:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes typing {
        0%, 60%, 100% { transform: translateY(0); }
        30% { transform: translateY(-10px); }
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables"""
    if 'agent' not in st.session_state:
        st.session_state.agent = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'initialized' not in st.session_state:
        st.session_state.initialized = False
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = 0
    if 'avg_response_time' not in st.session_state:
        st.session_state.avg_response_time = 0


def initialize_agent():
    """Initialize the HR Assistant Agent"""
    if not st.session_state.initialized:
        with st.spinner("Initializing HR Assistant Agent..."):
            try:
                load_dotenv()
                agent = HRAssistantAgent()
                agent.initialize()
                st.session_state.agent = agent
                st.session_state.initialized = True
                st.success("Agent initialized successfully!")
                return True
            except Exception as e:
                st.error(f"Error initializing agent: {str(e)}")
                return False
    return True


def display_header():
    """Display the header section"""
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">HR Assistant Agent</h1>
        <p class="header-subtitle">Your AI-powered HR companion for instant answers to policy, benefits, and leave queries</p>
        <center><span class="demo-badge">Demo Mode - Instant Responses</span></center>
    </div>
    """, unsafe_allow_html=True)


def display_chat_message(role: str, content: str):
    """Display a chat message with animation"""
    if role == "user":
        st.markdown(f'<div class="user-message"><strong>You:</strong><br>{content}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message"><strong>HR Assistant:</strong><br>{content}</div>', unsafe_allow_html=True)


def main():
    """Main application"""
    initialize_session_state()
    
    # Display header
    display_header()
    
    # Sidebar
    with st.sidebar:
        st.markdown("### Statistics")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-number">{st.session_state.total_questions}</p>
                <p class="stat-label">Questions Asked</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-number">{len(st.session_state.chat_history)}</p>
                <p class="stat-label">Conversations</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("### Quick Questions")
        
        categories = {
            "Leave Policies": [
                "How many sick leaves do I have?",
                "What is the maternity leave policy?",
                "Tell me about annual leave"
            ],
            "Benefits": [
                "What health insurance benefits do we get?",
                "Tell me about provident fund",
                "What bonuses do we get?"
            ],
            "Work Policies": [
                "When are the company holidays?",
                "What is the work from home policy?",
                "What is the notice period?"
            ]
        }
        
        for category, questions in categories.items():
            with st.expander(category):
                for question in questions:
                    if st.button(question, key=question, use_container_width=True):
                        st.session_state.current_question = question
        
        st.markdown("---")
        
        if st.button("Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.total_questions = 0
            if st.session_state.agent:
                st.session_state.agent.clear_history()
            st.rerun()
        
        st.markdown("---")
        st.markdown("""
        <div class="info-box">
            <h4>About This Agent</h4>
            <p>This AI agent demonstrates RAG (Retrieval Augmented Generation) architecture for answering HR queries.</p>
            <p><strong>Tech Stack:</strong></p>
            <ul>
                <li>Python & Streamlit</li>
                <li>LangChain Framework</li>
                <li>Vector Database (FAISS)</li>
                <li>Natural Language Processing</li>
            </ul>
            <p><strong>Features:</strong></p>
            <ul>
                <li>Instant responses</li>
                <li>Context-aware answers</li>
                <li>Beautiful UI/UX</li>
                <li>Conversation history</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #94a3b8; font-size: 0.85rem;">
            <p><strong>Built for</strong><br>Rooman AI Challenge 2024</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Initialize agent
    if not initialize_agent():
        st.stop()
    
    # Main chat interface
    st.markdown("### Chat with HR Assistant")
    
    # Display chat history
    for chat in st.session_state.chat_history:
        display_chat_message("user", chat["question"])
        display_chat_message("assistant", chat["answer"])
    
    # Chat input
    question = st.text_input(
        "Ask me anything about HR policies, benefits, leave, or holidays...",
        key="question_input",
        placeholder="e.g., How many sick leaves do I have?",
        value=st.session_state.get('current_question', '')
    )
    
    if 'current_question' in st.session_state:
        del st.session_state.current_question
    
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        ask_button = st.button("Ask Question", use_container_width=True)
    
    if ask_button and question:
        # Show typing indicator
        with st.spinner("Thinking..."):
            start_time = time.time()
            try:
                result = st.session_state.agent.ask(question)
                response_time = time.time() - start_time
                
                # Update stats
                st.session_state.total_questions += 1
                st.session_state.avg_response_time = (
                    (st.session_state.avg_response_time * (st.session_state.total_questions - 1) + response_time) 
                    / st.session_state.total_questions
                )
                
                # Add to chat history
                st.session_state.chat_history.append({
                    "question": question,
                    "answer": result["answer"],
                    "timestamp": datetime.now(),
                    "response_time": response_time
                })
                
                # Rerun to display new message
                st.rerun()
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    # Footer with enhanced info
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #94a3b8; padding: 1rem;">
        <p><strong>HR Assistant Agent</strong> - Powered by AI</p>
        <p style="font-size: 0.9rem;">Built for Rooman AI Agent Development Challenge 2024</p>
        <p style="font-size: 0.85rem; margin-top: 0.5rem;">
            Streamlit • LangChain • FAISS • Python
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
