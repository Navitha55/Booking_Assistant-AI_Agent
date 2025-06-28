# Booking_Assistant-AI_Agent
An AI-powered appointment booking assistant built with FastAPI, LangGraph, and Streamlit. It understands natural language, checks Google Calendar availability, and schedules meetings through a conversational interface. This project demonstrates seamless backend-agent-frontend integration with real-time intent handling and calendar event creation.

## AI Booking Assistant

An AI-powered appointment booking assistant using **FastAPI**, **LangGraph**, and **Streamlit**. It understands natural language like _"Schedule a call tomorrow at 3 PM"_, checks Google Calendar availability, and books meetings through a conversational chat interface.

## Prerequisites

- Python 3.8 or higher
- A Google Account
- Google Cloud Project with Calendar API enabled
- credentials.json file (OAuth 2.0 Client ID)

## Google Calendar Integration (OAuth Setup)

1. Go to: [Google Cloud Console](https://console.cloud.google.com/)
2. Create a **new project** (or use existing)
3. Enable **Google Calendar API**
4. Go to **APIs & Services → Credentials**
5. Click **“Create Credentials” → “OAuth Client ID”**
   - Application type: Desktop App
6. Download the credentials.json file

7. Go to **OAuth consent screen**
   - User Type: External
   - Add your email as a test user
   - Publish the app (in Testing mode is OK)

## Running the Project

1. **Start FastAPI server** (from root folder):
python -m uvicorn Backend.main:app --reload

2. **Start Streamlit app** (in new terminal):
streamlit run Frontend/app.py

## How It Works

- User types natural messages in the Streamlit chat interface
- Message is sent to FastAPI `/chat` endpoint
- LangGraph (mocked or real) analyzes the intent and date/time
- If intent is "book", the assistant:
  - Checks Google Calendar availability
  - Books the meeting
  - Replies with success or failure

##  Notes

- On first run, you'll be asked to **log in with your Google Account**
- A `token.json` will be created after authentication to avoid repeated logins
- All event times are scheduled in `Asia/Kolkata` timezone

##  License

MIT License. Free to use and modify.

## Output

![image](https://github.com/user-attachments/assets/bc3c34e9-d013-46d2-98ed-a6584020e42c)
