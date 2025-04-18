# 📞 AI Phone Call Assistant

A full-stack application for **interruptible**, **low-latency**, and **near-human quality AI phone calls** — seamlessly integrating Large Language Models (LLMs), speech understanding tools, text-to-speech systems, and Twilio’s phone API.

## 🎯 Summary

This project enables dynamic AI-driven phone calls that sound natural and responsive. It stitches together:

- 📞 **Twilio** for call handling
- 🗣️ **Deepgram** for real-time speech recognition
- 🤖 **OpenAI GPT-4o** or **Anthropic Claude 3.5 Sonnet** for conversation logic
- 🔈 **ElevenLabs** for lifelike speech synthesis
- ⚙️ A FastAPI server backend
- 🖥️ A Streamlit frontend to initiate and monitor calls

## 🚀 Features

| Component              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| ☎️ **Phone Service**    | Handles call flow using Twilio (make/receive calls)                        |
| 🗣️ **Speech-to-Text**   | Converts speech to text and detects when caller stops or interrupts (Deepgram) |
| 🤖 **LLM**              | Understands context and executes task-specific logic (GPT-4o / Claude 3.5) |
| 🔈 **Text-to-Speech**   | Generates high-quality speech responses (ElevenLabs)                       |
| ⚙️ **Backend (FastAPI)**| Web server handling audio streaming, call routing, and API endpoints        |
| 🖥️ **Frontend (Streamlit)**| Real-time call interface to monitor, start/stop, and view logs             |

## ⚙️ Installation

### 1. Clone & Install Dependencies

```bash
git clone https://github.com/your-username/ai-phone-call-assistant.git
cd ai-phone-call-assistant
pip install -r requirements.txt
```

*Optional: create a virtual environment to avoid conflicts.*

### 2. Setup ngrok

```bash
ngrok http 3000
```

Copy the generated URL (e.g., `https://1bf0-xxx.ngrok-free.app`) and use it in your `.env` file.

### 3. Configure Environment Variables

```bash
cp .env.example .env
```

Update `.env` with your credentials.

### 4. Configure Twilio Phone Number

```bash
twilio phone-numbers:update YOURNUMBER --voice-url=https://NGROKURL/incoming
```

### 5. Start the Backend (FastAPI)

```bash
python app.py
```
