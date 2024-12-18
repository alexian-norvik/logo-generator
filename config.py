import os
import logging

from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
logging.basicConfig(
    level=logging.getLevelNamesMapping()[LOGGING_LEVEL],
    format="%(asctime)s:%(name)s:%(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASYNC_OPENAI_INSTANCE = AsyncOpenAI(api_key=OPENAI_API_KEY)

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = "us-central1"
