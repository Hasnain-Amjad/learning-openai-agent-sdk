import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_api, set_default_openai_client, set_tracing_disabled
import asyncio

load_dotenv()

set_tracing_disabled(disabled=True)
set_default_openai_api("chat_completions")

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(client=client)

async def main():

    agent = Agent(
        name="Assistant",
        instructions= "you are helpful Assistant",
        model="gemini-2.0-flash"
    )

    result = await Runner.run(
        agent,
        "What is the capital of russia"
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

agent2 = Agent(
    name="Assistant",
    instructions= "you are helpful Assistant",
    model="gemini-2.0-flash"
)
