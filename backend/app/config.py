import os
from dotenv import load_dotenv
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BACKEND_DIR / ".env")
load_dotenv()

Groq_Api_key = (os.getenv("Groq_Api_key") or "").strip()
Groq_model = (os.getenv("Groq_model") or "").strip()
