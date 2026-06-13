# AgenticChatbot

A smart AI assistant demo built to showcase how an LLM can move beyond simple Q&A and act like an agent with reasoning, tool use, and workflow orchestration.

## Problem Solved
This project demonstrates how to build an AI chatbot that can:
- answer user questions in a conversational way,
- fetch live web information when needed,
- generate AI-powered news summaries,
- and present the experience through a clean Streamlit interface.

It is designed as a portfolio project to highlight practical AI engineering skills such as prompt-driven workflows, tool integration, and graph-based orchestration.

## What This Project Does
- Basic Chatbot: natural conversation with an LLM
- Chatbot with Web: uses Tavily search tools to answer with up-to-date information
- AI News: fetches and summarizes news into daily, weekly, or monthly reports

## Tech Stack
- Python
- Streamlit for the UI
- LangGraph for agent workflow orchestration
- LangChain / LangChain Groq for LLM integration
- Tavily for web search tools
- Groq models for fast AI responses

## Demo Flow
```text
User Input
   ↓
Streamlit UI
   ↓
Groq LLM setup
   ↓
LangGraph workflow
   ├─ Basic Chatbot
   ├─ Chatbot + Web Tools
   └─ AI News Summarizer
   ↓
Result displayed in the app
```

## Why This Is a Good Portfolio Project
- Shows real-world AI agent design, not just static prompt examples
- Demonstrates tool calling and stateful workflow logic
- Combines front-end UI, LLM orchestration, and external APIs in one app
- Easy to explain in interviews as a practical AI engineering demo

## How to Run
1. Install dependencies
   pip install -r requirements.txt
2. Start the app
   streamlit run app.py

## Future Improvements
- Add memory across chat sessions
- Support more external tools and APIs
- Improve UX with richer dashboards and response history

