from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")


class Config:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL = "gpt-5"

    TEMPERATURE = 0.7
