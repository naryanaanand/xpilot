from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")


class Config:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")

    REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")

    REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    MODEL = "gpt-5"
