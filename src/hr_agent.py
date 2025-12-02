"""
HR Assistant Agent - Demo Mode
Works without any API for demonstration purposes
Pre-configured responses based on actual HR documents
"""

from typing import List, Dict, Any
import time


class HRAssistantAgent:
    """AI Agent for answering HR-related queries - Demo Mode"""
    
    def __init__(self, temperature: float = 0.3):
        self.temperature = temperature
        self.chat_history = []
        self.demo_responses = {
            "sick leave": """According to the company policy, employees receive **12 days of paid sick leave per year**. Here are the key details:

- Sick leave does not carry forward to the next year
- Medical certificate required for sick leave exceeding 3 consecutive days
- Sick leave can be taken in half-day increments

If you need more information about leave policies, feel free to ask!""",
            
            "maternity": """Female employees are entitled to **26 weeks of paid maternity leave**. Here are the details:

- Must be taken within 8 weeks before and after delivery
- Can be extended by 4 weeks unpaid if required
- Requires medical documentation
- Maternity coverage: ₹75,000 per delivery under health insurance

For more specific information about your case, please contact HR directly.""",
            
            "holiday": """Here are the **national holidays for 2024**:

- January 26 - Republic Day
- March 25 - Holi
- August 15 - Independence Day
- October 2 - Gandhi Jayanti
- October 31 - Diwali
- December 25 - Christmas

Plus 15 more holidays throughout the year. You can also choose any **3 optional holidays** from a list that includes Makar Sankranti, May Day, and others.

Would you like the complete list of all holidays?""",
            
            "health insurance": """The company provides **comprehensive health insurance** with the following coverage:

**Coverage Details:**
- Annual Coverage: ₹5,00,000 per family per year
- Family Definition: Employee + Spouse + 2 dependent children
- Network: 5000+ hospitals across India
- Cashless Facility: Available at all network hospitals
- Reimbursement: Claims processed within 15 days

**Additional Benefits:**
- Dental Coverage: ₹25,000 per year
- Vision Coverage: ₹15,000 per year
- Annual Health Checkup: Free for employee and spouse
- Maternity Coverage: ₹75,000 per delivery

Would you like to know more about any specific benefit?""",
            
            "notice period": """The **notice period for resignation** is as follows:

**For Employees:**
- 60 days notice required
- 30 days notice during probation period

**For Company:**
- 60 days notice or payment in lieu

**Exit Process:**
- Submit resignation letter to manager and HR
- Complete exit interview
- Return all company property
- Handover responsibilities
- Full and final settlement within 45 days

Is there anything specific about the resignation process you'd like to know?""",
            
            "work from home": """The company offers **flexible work from home options**:

**Remote Work Policy:**
- Available 2 days per week with manager approval
- Full remote available for eligible roles
- Must maintain availability during core hours (10 AM - 4 PM)

**Support Provided:**
- Company laptop and VPN access
- Home office setup allowance: ₹15,000 (one-time)
- Broadband reimbursement: ₹1,000 per month

**Flexible Working Hours:**
- Core hours: 10 AM to 4 PM (mandatory presence)
- Flexible start: 8 AM to 10 AM
- Flexible end: 5 PM to 7 PM

Would you like more details about remote work policies?""",
            
            "annual leave": """Employees are entitled to **24 days of annual leave per year**:

**Key Details:**
- Annual leave accrues at 2 days per month
- Unused leave can be carried forward up to a maximum of 10 days
- Leave must be requested at least 2 weeks in advance for approval
- Annual leave is pro-rated for new joiners based on start date

**How to Apply:**
- Apply through HRMS portal
- Manager approval required
- HR notification automatic

Need help with anything else related to leave policies?""",

            "paternity": """Male employees receive **2 weeks of paid paternity leave**:

**Key Details:**
- Must be taken within 6 months of child's birth
- Requires birth certificate submission
- Can be taken continuously or in parts

For more information, please contact HR.""",

            "casual leave": """Employees receive **8 days of casual leave per year**:

**Key Details:**
- Can be taken without prior approval for emergencies
- Maximum 2 consecutive days at a time
- Cannot be combined with other leave types
- Does not carry forward to next year

Need help with anything else?""",

            "provident fund": """The company contributes to your **Provident Fund (PF)**:

**Contribution Details:**
- Company contributes 12% of basic salary to EPF
- Employee contribution: 12% of basic salary
- Voluntary PF contribution allowed
- Interest rate as per government norms (~8.15%)

**Gratuity:**
- Eligibility: After 5 years of service
- Calculation: 15 days salary for each completed year

Would you like more information about retirement benefits?""",

            "bonus": """The company offers **performance-based bonuses**:

**Annual Performance Bonus:**
- Up to 20% of annual salary
- Based on individual and company performance
- Paid in April each year

**Referral Bonus:**
- ₹25,000 per successful referral
- Payment after candidate completes 6 months
- Unlimited referrals

Want to know about other benefits?"""
        }
        
        # Conversational responses for casual messages
        self.conversational_responses = {
            # Greetings
            "greetings": {
                "patterns": ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "hola", "namaste"],
                "responses": [
                    """Hello! 👋 Welcome to the HR Assistant! I'm here to help you with all your HR-related questions.

I can assist you with:
- 🏖️ Leave policies (sick leave, annual leave, maternity/paternity)
- 💼 Benefits (health insurance, provident fund, bonuses)
- 📅 Company holidays and working hours
- 🏠 Work from home and flexible policies
- 📝 Resignation and notice period

What would you like to know today?""",
                    """Hi there! 😊 Great to see you! I'm your friendly HR Assistant, ready to help with any questions about company policies, benefits, or leave.

How can I assist you today?""",
                    """Hey! 👋 Welcome! I'm here to make your HR queries super easy to answer. Whether it's about leave, benefits, holidays, or policies - just ask away!

What brings you here today?"""
                ]
            },
            
            # Gratitude
            "gratitude": {
                "patterns": ["thank you", "thanks", "appreciate", "helpful", "great help"],
                "responses": [
                    """You're very welcome! 😊 I'm glad I could help! 

If you have any more questions about HR policies, benefits, or anything else, feel free to ask anytime. I'm here for you!""",
                    """Happy to help! 🌟 That's what I'm here for!

Don't hesitate to reach out if you need anything else. Have a great day!""",
                    """My pleasure! 😊 I'm always here to make your HR questions easier to answer.

Feel free to come back anytime you need assistance!"""
                ]
            },
            
            # Farewells
            "farewell": {
                "patterns": ["bye", "goodbye", "see you", "take care", "later", "gotta go"],
                "responses": [
                    """Goodbye! 👋 Take care and have a wonderful day!

Remember, I'm here 24/7 whenever you need help with HR questions. See you soon!""",
                    """See you later! 😊 Feel free to come back anytime you have questions.

Have a great day ahead!""",
                    """Take care! 🌟 It was great chatting with you!

I'll be here whenever you need assistance. Bye for now!"""
                ]
            },
            
            # Small talk - How are you
            "how_are_you": {
                "patterns": ["how are you", "how r u", "how are u", "what's up", "whats up", "wassup"],
                "responses": [
                    """I'm doing great, thank you for asking! 😊 I'm always excited to help with HR questions!

How about you? Is there anything I can help you with today?""",
                    """I'm fantastic! 🌟 Always ready to assist with your HR queries!

What can I help you with today?""",
                    """I'm doing wonderful, thanks! 😊 Just here, ready to make your HR questions easy to answer!

How can I assist you?"""
                ]
            },
            
            # About the bot
            "about": {
                "patterns": ["who are you", "what can you do", "what do you do", "help me", "capabilities", "what are you"],
                "responses": [
                    """I'm your friendly HR Assistant! 🤖 I'm here to help you with all things HR-related.

**What I can do:**
- 🏖️ Answer questions about leave policies (sick, annual, maternity, paternity, casual)
- 💼 Explain employee benefits (health insurance, PF, bonuses)
- 📅 Share company holiday schedules
- 🏠 Provide info on work from home and flexible policies
- 📝 Guide you through resignation and notice period procedures

**How to use me:**
Just ask your question in plain English! For example:
- "How many sick leaves do I have?"
- "What's the maternity leave policy?"
- "Tell me about health insurance"

What would you like to know?""",
                    """Hi! I'm the HR Assistant chatbot! 😊 Think of me as your 24/7 HR companion.

I can instantly answer questions about:
✅ All types of leave policies
✅ Employee benefits and insurance
✅ Company holidays
✅ Work policies and flexibility
✅ Resignation procedures

Just ask me anything HR-related, and I'll provide you with detailed, accurate information from our company policies!

What can I help you with?"""
                ]
            },
            
            # Acknowledgments
            "acknowledgment": {
                "patterns": ["ok", "okay", "cool", "nice", "great", "awesome", "perfect", "got it", "understood", "alright"],
                "responses": [
                    """Great! 😊 Is there anything else you'd like to know about HR policies or benefits?

I'm here to help!""",
                    """Awesome! 🌟 Feel free to ask if you have any other questions!

I'm always here to assist.""",
                    """Perfect! 👍 Let me know if you need anything else.

Happy to help anytime!"""
                ]
            }
        }
        
    def initialize(self):
        """Initialize the agent - Demo Mode"""
        print("Initializing HR Assistant Agent (Demo Mode)...")
        # Simulate initialization delay
        time.sleep(0.5)
        print("Agent initialized successfully!")
        
    def ask(self, question: str) -> Dict[str, Any]:
        """
        Ask a question to the HR Assistant - Demo Mode
        
        Args:
            question: User's question
            
        Returns:
            Dictionary with answer and source documents
        """
        import random
        
        question_lower = question.lower().strip()
        answer = None
        
        # First, check for conversational patterns
        for category, data in self.conversational_responses.items():
            for pattern in data["patterns"]:
                if pattern in question_lower:
                    # Randomly select a response for variety
                    answer = random.choice(data["responses"])
                    break
            if answer:
                break
        
        # If no conversational match, check HR-specific queries
        if not answer:
            for keyword, response in self.demo_responses.items():
                if keyword in question_lower:
                    answer = response
                    break
        
        # Default response if no match - check if it's HR-related or not
        if not answer:
            # HR-related keywords to detect if question is at least HR-related
            hr_keywords = [
                'leave', 'holiday', 'vacation', 'sick', 'annual', 'maternity', 'paternity', 'casual',
                'benefit', 'insurance', 'health', 'medical', 'provident', 'pf', 'epf', 'bonus', 'salary',
                'pay', 'compensation', 'allowance', 'reimbursement', 'claim',
                'policy', 'policies', 'hr', 'human resource', 'employee', 'staff', 'work',
                'office', 'company', 'organization', 'job', 'employment', 'resign', 'resignation',
                'notice', 'period', 'joining', 'onboarding', 'exit', 'termination',
                'remote', 'wfh', 'work from home', 'flexible', 'hours', 'timing', 'shift',
                'training', 'development', 'performance', 'appraisal', 'review', 'promotion',
                'referral', 'recruitment', 'hiring', 'probation', 'contract', 'permanent'
            ]
            
            # Check if question contains any HR-related keywords
            is_hr_related = any(keyword in question_lower for keyword in hr_keywords)
            
            if is_hr_related:
                # Question seems HR-related but we don't have specific info
                answer = """Thank you for your question! I can help you with HR-related information, but I need a bit more clarity.

I specialize in:
- **Leave policies**: sick leave, annual leave, maternity/paternity leave, casual leave
- **Benefits**: health insurance, provident fund, bonuses, referral programs
- **Company holidays** and working hours
- **Work from home** and flexible working policies
- **Resignation** and notice period procedures

Could you please rephrase your question or ask about one of these specific topics? I'll be happy to provide detailed information!"""
            else:
                # Question is not HR-related at all
                answer = """I appreciate your question, but I'm specifically designed to help with **HR-related queries only**. 😊

I can assist you with:
- 🏖️ **Leave policies** (sick leave, annual leave, maternity/paternity leave)
- 💼 **Employee benefits** (health insurance, provident fund, bonuses)
- 📅 **Company holidays** and working schedules
- 🏠 **Work from home** and flexible policies
- 📝 **Resignation procedures** and notice periods

Please feel free to ask me anything related to HR policies, benefits, or workplace matters, and I'll be happy to help!"""
        
        # Store in chat history
        self.chat_history.append({
            "question": question,
            "answer": answer
        })
        
        return {
            "answer": answer,
            "source_documents": [],
            "question": question
        }
    
    def get_chat_history(self) -> List[Dict[str, str]]:
        """Get the conversation history"""
        return self.chat_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.chat_history = []
        print("Conversation history cleared")
