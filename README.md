# AI-Powered Chatbot

A lightweight retrieval-based chatbot developed using Python and Flask, designed to provide instant responses to common customer queries through an interactive web interface.

## Overview

The AI Chatbot demonstrates how predefined input patterns and response matching can be used to build an automated customer support assistant.

It identifies user queries based on predefined keywords and patterns, retrieves the most relevant response, and delivers it instantly through a website-based chat interface.

## Features

- **Automated Responses:** Provides instant answers to predefined customer queries.
- **Pattern Matching:** Identifies user intent using predefined keywords and patterns.
- **Interactive Chat Interface:** Provides a user-friendly browser-based messaging experience.
- **Customer Support Automation:** Handles common commercial inquiries.
- **Fallback Responses:** Responds appropriately when a query is not recognized.
- **REST API:** Provides a JSON-based chat endpoint for frontend communication.
- **Lightweight Architecture:** Built with Flask and Python.

## Supported Query Categories

| Category | Example |
|---|---|
| Greetings | Hello, Hi, Hey |
| Pricing | What are your pricing plans? |
| Business Hours | What are your support hours? |
| Contact | How can I contact support? |
| Refunds | I want a refund |
| Services | What features do you offer? |

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web framework and API |
| HTML | Chat interface |
| CSS | Interface styling |
| JavaScript | Frontend interaction |
| JSON | Client-server communication |

## How It Works

1. A user enters a message through the chatbot interface.
2. JavaScript sends the message to the Flask backend.
3. The backend processes the input and identifies matching predefined patterns.
4. The chatbot selects the corresponding response.
5. The response is returned through a JSON API.
6. The frontend displays the response instantly in the chat window.

## Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/sameerkhanio/CodeAlpha_AIChatbot.git
cd CodeAlpha_AIChatbot
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the environment**

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the application**

```bash
python app.py
```

**6. Open in your browser**

http://127.0.0.1:5001

## API Endpoint

**POST** `/chat`

Example request:

```json
{
  "message": "What are your pricing plans?"
}
```

Example response:

```json
{
  "reply": "Our demo plans are Basic (free), Pro ($9/month), and Business ($29/month). Contact sales for a custom quote."
}
```

## Project Structure

```text
CodeAlpha_AIChatbot/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Internship Project

Developed as part of the **CodeAlpha Cloud Computing Internship**.

**Author:** Muhammad Sameer Khan

**GitHub:** https://github.com/sameerkhanio

---

*This project demonstrates a retrieval-based chatbot architecture using predefined patterns. It does not use a generative AI model or machine learning training pipeline.*
