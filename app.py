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

# Custom CSS for stunning premium UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main theme colors */
    :root {
        --primary: #6366f1;
        --primary-dark: #4f46e5;
        --secondary: #8b5cf6;
        --accent: #ec4899;
        --success: #10b981;
        --bg-dark: #0a0e1a;
        --bg-surface: #111827;
        --bg-elevated: #1f2937;
        --text-primary: #f9fafb;
        --text-secondary: #9ca3af;
        --glow: rgba(99, 102, 241, 0.4);
    }
    
    /* Animated gradient background */
    .main {
        background: linear-gradient(135deg, #0a0e1a 0%, #1a1f35 50%, #0a0e1a 100%);
        background-size: 200% 200%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Glassmorphism Header */
    .header-container {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.9) 0%, rgba(139, 92, 246, 0.9) 100%);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 3rem 2rem;
        border-radius: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 
            0 20px 60px rgba(99, 102, 241, 0.4),
            0 0 0 1px rgba(255, 255, 255, 0.1) inset;
        animation: fadeInDown 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
    }
    
    .header-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    @keyframes fadeInDown {
        from { 
            opacity: 0; 
            transform: translateY(-30px) scale(0.95);
        }
        to { 
            opacity: 1; 
            transform: translateY(0) scale(1);
        }
    }
    
    .header-title {
        color: white;
        font-size: 3rem;
        font-weight: 800;
        margin: 0;
        text-align: center;
        letter-spacing: -0.02em;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        position: relative;
        z-index: 1;
    }
    
    .header-subtitle {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.2rem;
        text-align: center;
        margin-top: 0.75rem;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }
    
    .demo-badge {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        color: white;
        padding: 0.6rem 1.5rem;
        border-radius: 2rem;
        font-size: 0.95rem;
        font-weight: 600;
        display: inline-block;
        margin-top: 1.25rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.2);
        position: relative;
        z-index: 1;
    }
    
    /* Premium Chat Messages */
    .user-message {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        padding: 1.25rem 1.75rem;
        border-radius: 1.5rem 1.5rem 0.5rem 1.5rem;
        margin: 1.25rem 0;
        box-shadow: 
            0 8px 24px rgba(99, 102, 241, 0.35),
            0 0 0 1px rgba(255, 255, 255, 0.1) inset;
        animation: slideInRight 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        font-size: 1.05rem;
        line-height: 1.6;
        position: relative;
        overflow: hidden;
    }
    
    .user-message::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.5), transparent);
    }
    
    @keyframes slideInRight {
        from { 
            opacity: 0; 
            transform: translateX(30px) scale(0.95);
        }
        to { 
            opacity: 1; 
            transform: translateX(0) scale(1);
        }
    }
    
    .assistant-message {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        color: #f9fafb;
        padding: 1.25rem 1.75rem;
        border-radius: 1.5rem 1.5rem 1.5rem 0.5rem;
        margin: 1.25rem 0;
        border-left: 4px solid #6366f1;
        box-shadow: 
            0 8px 24px rgba(0, 0, 0, 0.4),
            0 0 0 1px rgba(99, 102, 241, 0.2) inset;
        animation: slideInLeft 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        font-size: 1.05rem;
        line-height: 1.7;
        backdrop-filter: blur(10px);
    }
    
    @keyframes slideInLeft {
        from { 
            opacity: 0; 
            transform: translateX(-30px) scale(0.95);
        }
        to { 
            opacity: 1; 
            transform: translateX(0) scale(1);
        }
    }
    
    /* Glassmorphism Stats Cards */
    .stat-card {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 1.75rem;
        border-radius: 1.25rem;
        text-align: center;
        box-shadow: 
            0 8px 32px rgba(99, 102, 241, 0.2),
            0 0 0 1px rgba(99, 102, 241, 0.3) inset;
        color: white;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    .stat-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 
            0 16px 48px rgba(99, 102, 241, 0.35),
            0 0 0 1px rgba(99, 102, 241, 0.5) inset;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.25) 0%, rgba(139, 92, 246, 0.25) 100%);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        background: linear-gradient(135deg, #fff 0%, #e0e7ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-label {
        font-size: 0.95rem;
        opacity: 0.9;
        margin-top: 0.5rem;
        font-weight: 500;
        letter-spacing: 0.02em;
    }
    
    /* Premium Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        border: none;
        padding: 0.875rem 2.5rem;
        border-radius: 0.75rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 
            0 8px 24px rgba(99, 102, 241, 0.35),
            0 0 0 1px rgba(255, 255, 255, 0.1) inset;
        letter-spacing: 0.01em;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 
            0 12px 32px rgba(99, 102, 241, 0.45),
            0 0 0 1px rgba(255, 255, 255, 0.2) inset;
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
    }
    
    .stButton>button:active {
        transform: translateY(-1px) scale(0.98);
    }
    
    /* Enhanced Chat Input */
    .stChatInput>div>div>input {
        background: rgba(31, 41, 55, 0.8);
        backdrop-filter: blur(10px);
        color: #f9fafb;
        border: 2px solid rgba(99, 102, 241, 0.3);
        border-radius: 1rem;
        padding: 1rem 1.25rem;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    }
    
    .stChatInput>div>div>input:focus {
        border-color: #6366f1;
        box-shadow: 
            0 0 0 4px rgba(99, 102, 241, 0.15),
            0 8px 24px rgba(0, 0, 0, 0.3);
        background: rgba(31, 41, 55, 0.95);
    }
    
    /* Glassmorphism Info Boxes */
    .info-box {
        background: linear-gradient(135deg, rgba(31, 41, 55, 0.6) 0%, rgba(17, 24, 39, 0.6) 100%);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 1.75rem;
        border-radius: 1.25rem;
        border-left: 4px solid #6366f1;
        margin: 1.25rem 0;
        color: #f9fafb;
        box-shadow: 
            0 8px 24px rgba(0, 0, 0, 0.3),
            0 0 0 1px rgba(99, 102, 241, 0.2) inset;
    }
    
    .info-box h4 {
        color: #e0e7ff;
        font-weight: 700;
        margin-bottom: 1rem;
        font-size: 1.15rem;
    }
    
    /* Premium Scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #111827;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 10px;
        border: 2px solid #111827;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0e1a 0%, #111827 100%);
        border-right: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: rgba(99, 102, 241, 0.1);
        border-radius: 0.75rem;
        font-weight: 600;
        color: #e0e7ff;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(99, 102, 241, 0.2);
        transform: translateX(4px);
    }
    
    /* Smooth transitions for all elements */
    * {
        transition: background 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    /* Glow effect on hover for interactive elements */
    .stButton>button:hover,
    .stat-card:hover {
        filter: drop-shadow(0 0 20px var(--glow));
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
    
    # Display chat history
    for chat in st.session_state.chat_history:
        display_chat_message("user", chat["question"])
        display_chat_message("assistant", chat["answer"])
    
    # Chat input
    # Handle quick question clicks from sidebar
    if 'current_question' in st.session_state:
        question = st.session_state.current_question
        del st.session_state.current_question
        # Process the question immediately
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
    
    # Chat input section
    st.markdown("### Chat with HR Assistant")
    
    # Use chat_input which automatically clears after submission
    question = st.chat_input(
        "Ask me anything about HR policies, benefits, leave, or holidays...",
        key="question_input"
    )
    
    if question:
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
    



if __name__ == "__main__":
    main()
