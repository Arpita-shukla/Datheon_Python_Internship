import re

INTENTS = [
    {
        "patterns": [r"\b(hi|hello|hey|greetings|namaste)\b"],
        "response": "Hello! Welcome to Datheon Support Assistant. How can I help you today?"
    },
    {
        "patterns": [r"\b(hours|timing|open|close|schedule|time)\b"],
        "response": "Our support team is available Monday to Friday, from 9:00 AM to 6:00 PM IST."
    },
    {
        "patterns": [r"\b(internship|certificate|task|submit|github|verification)\b"],
        "response": "To get your verified certificate, complete at least 2-3 tasks, push them to a public GitHub repository, and submit the link on the Datheon portal."
    },
    {
        "patterns": [r"\b(fee|cost|price|free|charge)\b"],
        "response": "The Datheon internship evaluation and certificate verification have zero evaluation fee."
    },
    {
        "patterns": [r"\b(contact|email|support|help|reach)\b"],
        "response": "You can reach our team anytime at hello@datheon.in."
    }
]

EXIT_COMMANDS = {"bye", "exit", "quit"}

def get_response(user_input):
    cleaned_input = user_input.lower().strip()
    for intent in INTENTS:
        for pattern in intent["patterns"]:
            if re.search(pattern, cleaned_input):
                return intent["response"]
    return "I'm sorry, I didn't quite understand that. You can ask about business hours, internship tasks, certificate fees, or contact details."

def run_chatbot():
    print("=== Datheon Interactive Terminal Assistant ===")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.\n")

    while True:
        user_msg = input("You: ").strip()
        if not user_msg:
            continue

        if user_msg.lower() in EXIT_COMMANDS:
            print("Bot: Thank you for chatting! Have a great day ahead. Goodbye!")
            break

        reply = get_response(user_msg)
        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    run_chatbot()
  
