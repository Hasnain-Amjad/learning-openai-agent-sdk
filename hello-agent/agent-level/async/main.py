import os
import asyncio
from dotenv import load_dotenv
# from openai import AsyncOpenAI
from agents import Agent

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

