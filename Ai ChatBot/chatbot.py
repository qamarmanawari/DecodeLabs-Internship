# ===================PROJECT 1=================================
# PROJECT 1: RULE-BASED AI CHATBOT
# DecodeLabs Internship | Batch 2026 | Powered by DecodeLabs
# ============================================================

import random   

responses = {
    # --- Greetings ---
    'hello': [
        'Hi there! Welcome to DecodeLabs. How can I help you today?',
        'Hello! Great to see you.',
        'Hey! DecodeBot at your service.',
        'Hi! What can I do for you today?',
    ],
    'hi': [
        'Hello! Great to see you. What can I do for you?',
        'Hi there! Ready to chat.',
        'Hey! How is your day going?',
    ],
    'hey': [
        'Hey! I am DecodeBot. Ask me anything.',
        'Hello there! What is on your mind?',
        'Hey! Good to see you.',
    ],
    'good morning': [
        'Good morning! Ready to build some AI?',
        'Morning! Let us make today productive.',
        'Good morning! Coffee in hand? Let us code.',
    ],
    'good evening': [
        'Good evening! Hope your day went well.',
        'Evening! Time to relax or code — your call.',
        'Good evening! What brings you here?',
    ],

    # --- About the Bot ---
    'what is your name': [
        'I am DecodeBot, your rule-based AI assistant.',
        'My name is DecodeBot. Nice to meet you!',
        'They call me DecodeBot. Built with pure Python logic.',
    ],
    'who are you': [
        'I am a deterministic chatbot built with pure Python logic.',
        'I am DecodeBot — a rule-based AI, no neural networks here.',
        'Just a humble chatbot made of if-else logic and dictionaries.',
    ],
     'What is your name': [
            'I am a deterministic chatbot, you can call me DecodeBot built with pure Python logic.',
            'I am DecodeBot — a rule-based AI, no neural networks here.',
            'DecodeBot- Just a humble chatbot made of if-else logic and dictionaries.',
        ],
    'what can you do': [
        'I can respond to greetings, answer basic questions, and chat. Try saying "help".',
        'I handle greetings, small talk, and a few facts. Type "help" for a list.',
        'I reply to predefined inputs. Say "help" to see what I know.',
    ],
    'help': [
        'You can try: hello, hi, how are you, what is your name, what can you do, bye, exit.',
        'Try saying: hello, hi, how are you, who are you, thanks, bye.',
        'Available commands: hello, hi, hey, how are you, what is your name, help, bye, exit.',
    ],
    'how are you': [
        'I am running at peak efficiency. Thanks for asking!',
        'All systems operational. How about you?',
        'Fantastic! Zero bugs today (so far).',
        'I am great — 100% uptime since you started chatting.',
    ],
    'are you human': [
        'No, I am a rule-based program. 100% logic, 0% magic.',
        'Nope — just code. No coffee breaks needed.',
        'I am a chatbot. Humans are far more interesting.',
    ],

    # --- Internship / DecodeLabs ---
    'what is decodelabs': [
        'DecodeLabs is your AI training ground. Batch 2026 — let\'s go!',
        'DecodeLabs is where interns become AI engineers. Welcome aboard!',
        'A training platform for future AI engineers. You are in the right place.',
    ],
    'what is project 1': [
        'Project 1 is the Rule-Based AI Chatbot — your foundation phase.',
        'Project 1 teaches control flow and logic via a rule-based chatbot.',
        'It is your first milestone: build a chatbot using pure if-else logic.',
    ],
    'who made you': [
        'I was built by an AI intern at DecodeLabs as part of Project 1.',
        'An intern at DecodeLabs created me for Project 1.',
        'A fellow intern — just like you — wrote my code.',
    ],

    # --- Gratitude / Politeness ---
    'thanks': [
        'You are welcome! Happy to help.',
        'Anytime! That is what I am here for.',
        'No problem at all.',
        'Glad I could help!',
    ],
    'thank you': [
        'Anytime! That is what I am here for.',
        'You are most welcome.',
        'Happy to be of service.',
    ],
    'sorry': [
        'No worries at all. We all make typos.',
        'It is completely fine.',
        'No need to apologize — we are just chatting.',
    ],

    # --- Exit Commands ---
    'bye': [
        'Goodbye! Have a great day ahead.',
        'See you next time!',
        'Bye! Come back soon.',
    ],
    'exit': [
        'Shutting down. Goodbye!',
        'Session ended. Take care!',
        'Powering off. See you next time!',
    ],
    'quit': [
        'Session ended. See you next time!',
        'Quitting now. Goodbye!',
        'Exiting. Have a great day!',
    ],
}

# ------------------------------------------------------------
# STEP 2: STARTUP BANNER
# ------------------------------------------------------------
print("=" * 55)
print("  DecodeBot v1.1 — Rule-Based AI Chatbot")
print("  Powered by DecodeLabs | Batch 2026")
print("=" * 55)
print("Type 'help' to see what I can do. Type 'exit' to quit.\n")

# ------------------------------------------------------------
# STEP 3: THE INFINITE LOOP 
# ------------------------------------------------------------
while True:

    # --- 3a. INPUT & SANITIZATION (Page 10) ---
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()

    # --- 3b. HANDLE EMPTY INPUT ---
    if clean_input == "":
        print("DecodeBot: Please type something. Try 'help' if you're stuck.\n")
        continue

    # --- 3c. KILL COMMAND (Exit Strategy — Page 17) ---
    if clean_input in ('exit', 'quit', 'bye'):
        print(f"DecodeBot: {random.choice(responses[clean_input])}")
        break

    # --- 3d. LOOKUP + FALLBACK (Page 15) ---
    # If key exists -> pick a random reply from its list
    # If key missing -> use the fallback string
    if clean_input in responses:
        reply = random.choice(responses[clean_input])
    else:
        reply = "I do not understand. Try saying 'help'."

    print(f"DecodeBot: {reply}\n")

# ------------------------------------------------------------
# STEP 4: SHUTDOWN MESSAGE
# ------------------------------------------------------------
print("=" * 55)
print("  Session terminated. Thanks for chatting!")
print("=" * 55)