```markdown
# 🤖 Project 1: Rule-Based AI Chatbot

**DecodeLabs Internship | Batch 2026**

A deterministic, white-box chatbot built with pure Python logic — no ML, no hallucinations.

---

## 🎯 Features

- Continuous input loop (`while True`)
- Input sanitization (lowercase + strip)
- Dictionary knowledge base — O(1) lookup
- Randomized responses for variety
- Fallback for unknown inputs
- Clean exit (`exit` / `quit` / `bye`)

---

## 🚀 How to Run

```bash
python chatbot.py
```

Type `help` to see commands. Type `exit` to quit.

---

## 💬 Sample Session

```
You: hello
DecodeBot: Hey! DecodeBot at your service.

You: how are you
DecodeBot: All systems operational. How about you?

You: blah blah
DecodeBot: I do not understand. Try saying 'help'.

You: exit
DecodeBot: Session ended. Take care!
```

---

## 📂 Files

| File | Purpose |
|------|---------|
| `chatbot.py` | Main chatbot program |
| `README.md` | This file |

---

## 🧠 Key Concepts

- Control flow (`while`, `if/else`)
- Dictionaries (O(1) lookup vs O(n) if-elif)
- `random.choice()` for varied replies
- String methods (`.lower()`, `.strip()`)

---

## 🛡️ Why Rule-Based AI?

- **Traceable** — Input → Logic → Output
- **Safe** — Zero hallucination risk
- **Compliant** — Required in Finance & Healthcare

> *"An LLM without rules is a hallucination engine."*

---

## 👨‍💻 Author

**Qamar Abbas Shahzad** — AI Intern, DecodeLabs Batch 2026

---

*Built with pure Python logic.* 🤖
```

