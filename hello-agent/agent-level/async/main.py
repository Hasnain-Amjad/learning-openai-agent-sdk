import os
import asyncio
from dotenv import load_dotenv
# from openai import AsyncOpenAI
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

async def main():
    
    agent = Agent(
        name="Assistant",
        instructions="You are helpful Assistant",
        model= model
    )

    result =await Runner.run(
        agent,
        "what is the capital of pakistan"
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())