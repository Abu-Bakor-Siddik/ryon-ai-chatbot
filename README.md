# Ryon AI – WhatsApp Auto Reply Chatbot

**Ryon AI** is a Python-based WhatsApp auto-reply chatbot that uses Google's Gemini AI to generate natural, human-like responses to incoming WhatsApp messages.

It connects to WhatsApp Web through Playwright, monitors incoming messages from a selected conversation, and automatically generates and sends replies using the Gemini API.

The goal of this project is to build a simple personal AI assistant that can handle WhatsApp conversations with a friendly, witty, and conversational personality.

---

## Features

- **AI-Powered Replies:** Uses Google's Gemini API to generate intelligent responses.
- **WhatsApp Web Integration:** Connects to WhatsApp Web using Playwright.
- **Automatic Message Monitoring:** Monitors a selected conversation for new incoming messages.
- **Automatic Reply:** Generates and sends replies without requiring manual confirmation.
- **Conversation Context:** Uses recent chat history to generate more relevant responses.
- **Custom AI Personality:** Configured to respond in a friendly, funny, witty, and natural American English style.
- **Persistent Login:** Saves the WhatsApp browser session locally to avoid scanning the QR code every time.
- **Custom Monitoring Duration:** Allows users to choose how long the chatbot should monitor a conversation.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Google Gemini API | AI-powered response generation |
| Playwright | Browser automation |
| Chromium | Runs WhatsApp Web |
| python-dotenv | Manages environment variables |
| Regular Expressions | Extracts message information |

---

## 📁 Project Structure

```text
Ryon-AI-Chatbot/
│
├── main.py              # Main application controller
├── browser.py           # WhatsApp Web browser connection
├── chat_reader.py       # Reads and processes WhatsApp messages
├── ai.py                # Gemini AI response generation
│
├── requirements.txt     # Python dependencies
├── .env                 # API credentials (not uploaded to GitHub)
├── .gitignore           # Excludes sensitive and unnecessary files
│
├── whatsapp_profile/    # Saved WhatsApp browser session
└── .venv/               # Python virtual environment
```

---

## ⚙️ Requirements

Before starting, make sure you have:

- Python 3.10 or newer
- Google Gemini API key
- Google Chrome/Chromium-compatible system
- An active WhatsApp account
- Internet connection
- Git

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Abu-Bakor-Siddik/Ryon-AI-Chatbot.git
```

Navigate to the project directory:

```bash
cd Ryon-AI-Chatbot
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it on Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Chromium

```bash
playwright install chromium
```

On Linux, if required, install the browser dependencies:

```bash
playwright install-deps chromium
```

---

## Gemini API Configuration

Ryon AI uses Google's Gemini API to generate responses.

### Step 1: Get Your API Key

Visit Google AI Studio:

https://aistudio.google.com/apikey

Sign in with your Google account and create an API key.

### Step 2: Create a `.env` File

Create a file named `.env` in the root project directory.

Add the following:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.5-flash-lite
```

Replace `your_gemini_api_key_here` with your actual API key.

**Important:** Never share your API key or upload your `.env` file to GitHub.

---

## Connecting WhatsApp

1. Run the application.
2. A Chromium browser window will open.
3. Navigate to WhatsApp Web if it does not open automatically.
4. Scan the QR code using your WhatsApp mobile application if required.
5. Wait until WhatsApp Web is fully loaded.
6. Press Enter in the terminal when prompted.
7. Open the WhatsApp conversation you want Ryon AI to monitor.

The browser session is saved locally in the `whatsapp_profile/` directory.

You generally won't need to scan the QR code again unless the session expires or you remove the saved profile.

---

## How to Run

Make sure your virtual environment is activated.

Run:

```bash
python3 main.py
```

Follow the terminal instructions.

### Example Workflow

```text
Waiting for WhatsApp Web...
Scan the QR code if required, then press Enter...

WhatsApp Web is ready!
WhatsApp connected successfully!

Open the WhatsApp conversation you want to monitor.

Monitoring duration (minutes): 5

Monitoring started...
New incoming message detected!

Generating AI response...
Ryon: Hey! What's up?

Reply sent successfully!
```

*The terminal output may vary depending on the application version.*

Once monitoring starts:

1. Open the conversation you want to monitor.
2. Ryon AI checks for new incoming messages.
3. The message history is sent to Gemini for context.
4. Gemini generates a response.
5. Ryon AI automatically sends the generated reply.

To stop monitoring, wait for the selected duration to finish or interrupt the application using `Ctrl + C`.

---

## How It Works

Ryon AI follows a simple workflow:

```text
       WhatsApp Web
             |
             v
       Playwright Browser
             |
             v
       Monitor Messages
             |
             v
       Detect New Incoming Message
             |
             v
       Read Recent Chat History
             |
             v
       Google Gemini API
             |
             v
       Generate AI Response
             |
             v
       Send Reply Automatically
```

### Main Components

**1. `main.py`**
- Controls the complete application.
- Starts WhatsApp monitoring.
- Detects new incoming messages.
- Calls the AI response generator.
- Sends replies automatically.

**2. `browser.py`**
- Launches Chromium using Playwright.
- Opens WhatsApp Web.
- Maintains the browser session.

**3. `chat_reader.py`**
- Reads recent WhatsApp messages.
- Extracts message text and sender information.
- Identifies incoming and outgoing messages.

**4. `ai.py`**
- Connects to Google's Gemini API.
- Processes recent conversation history.
- Generates natural-language responses.

---

## Customize Ryon's Personality

You can customize Ryon's personality by editing the system instructions or prompt inside `ai.py`.

For example:

- Friendly and helpful assistant
- Funny and sarcastic chatbot
- Professional business assistant
- Casual conversational AI
- Short and direct responder

You can also change the response length, language, and communication style.

---

## Dependencies

The project uses the following main Python packages:

- `playwright`
- `google-genai`
- `python-dotenv`

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

##  Troubleshooting

### 1. Gemini API Key Not Found

**Problem:**
```text
ValueError: Gemini API key not found in .env
```

**Solution:**
- Make sure `.env` exists in the project root.
- Check that `GEMINI_API_KEY` is correctly written.
- Make sure you are running the application from the project directory.

### 2. WhatsApp Web Not Connecting

**Solution:**
- Check your internet connection.
- Scan the QR code again if required.
- Make sure WhatsApp Web is fully loaded before pressing Enter.

### 3. Playwright Browser Not Found

**Problem:** Chromium is not installed.

**Solution:**

```bash
playwright install chromium
```

### 4. No Automatic Reply

**Solution:**
- Make sure the correct conversation is open.
- Check whether a new incoming message has arrived.
- Check your Gemini API key and API quota.
- Make sure automatic sending is enabled in `main.py`.

---

##  Security & Privacy

- Keep your Gemini API key private.
- Never upload `.env` to GitHub.
- Do not share your `whatsapp_profile/` directory.
- The browser profile contains your WhatsApp login session.
- Be careful when using automatic replies in personal or professional conversations.
- Review generated messages and use the chatbot responsibly.

**Note:** This project is an independent personal project and is not affiliated with or officially endorsed by WhatsApp, Meta, or Google.

---

##  Disclaimer

Ryon AI is an experimental personal automation project developed for learning and educational purposes.

It uses browser automation to interact with WhatsApp Web. Changes to WhatsApp Web may affect its functionality. Automated messaging may also be subject to WhatsApp's terms and policies.

Use it responsibly and avoid sending unwanted or misleading messages.

---

##  Future Improvements

- [ ] Support multiple WhatsApp conversations.
- [ ] Add a dashboard to manage chatbot settings.
- [ ] Add custom reply modes.
- [ ] Improve message detection and handling.
- [ ] Add conversation-specific AI personalities.
- [ ] Add message logging and monitoring.
- [ ] Add voice message support.

---

##  Developer

**Abu Bakor Siddik**

Computer Science & Engineering Student  
University of Liberal Arts Bangladesh (ULAB)

- GitHub: https://github.com/Abu-Bakor-Siddik

---

⭐ If you find this project interesting, consider giving the repository a star!

**Built with Python, Playwright, and Google Gemini AI.**
