 # 🎥 AI Video Creation Chatbot

An intelligent agent powered by **Groq**, **LangGraph**, **FastAPI**, and **Tavily** that automates the entire video creation process — from user prompt to AI-written script, voice-over, and final rendered video, all optimized for social media platforms like **TikTok**, **Instagram Reels**, and **YouTube Shorts**.

---

## 📌 Features

- 🧠 **Chatbot Agent** built with LangGraph to handle multi-step workflows
- 🔍 **Web Search Integration** using Tavily API for fact-rich script generation
- ✍️ **Script Writing** via Groq's blazing-fast LLaMA 3 API
- 🗣️ **Voice-over Generation** using TTS (gTTS or optional Bark)
- 🎬 **Video Rendering** with FFmpeg & MoviePy
- ⚙️ **FastAPI Backend** to serve and manage chatbot requests
- 📦 Docker-ready for easy deployment





install python version
uv python install pypy-3.11.13-windows-x86_64-none  
E:\Video_Making_Agent>uv venv env --python=3.11
Using CPython 3.11.5
Creating virtual environment at: env
Activate with: env\Scripts\activate
.\env\Scripts\activate
pip install -U langchain langchain-openai

LANGSMITH_TRACING="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="<your-api-key>"
LANGSMITH_PROJECT="pr-reflecting-chauffeur-83"
OPENAI_API_KEY="<your-openai-api-key>"
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
llm.invoke("Hello, world!")
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-70b-versatile",  # example Groq model
    temperature=0
)

print(llm.invoke("Hello, world!"))
