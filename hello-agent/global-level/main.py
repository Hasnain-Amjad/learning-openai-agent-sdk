import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_api, set_default_openai_client, set_tracing_disabled
import 
load_dotenv()

set_tracing_disabled(disabled=True)
set_default_openai_api("chat_completions")

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(client=client)

agent = Agent(
    name="Assistant",
    instructions= "you are helpful Assistant"
)

result = Runner.run_sync(
    agent,
    "What is the capital of russia"
)
