import os
import asyncio
from dotenv import load_dotenv
# from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=client
# )

agent = Agent(
    name= "basic-agent",
    instructions= "you are helpful assistant",
    model= OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)
    )

output = Runner.run_sync(
    agent,
    "who is founder of pakistan"
)

print(output.final_output)