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
        question_lower = question.lower()
        
        # Match question to demo responses
        answer = None
        for keyword, response in self.demo_responses.items():
            if keyword in question_lower:
                answer = response
                break
        
        # Default response if no match
        if not answer:
            answer = """Thank you for your question! Based on the company's HR policies, I can help you with information about:

- **Leave policies**: sick leave, annual leave, maternity/paternity leave, casual leave
- **Benefits**: health insurance, provident fund, bonuses, training
- **Company holidays** and working hours
- **Work from home** and flexible working policies
- **Resignation** and notice period

Please ask a more specific question, and I'll provide detailed information from our HR documents."""
        
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
