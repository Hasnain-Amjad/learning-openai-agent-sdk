import os
import asyncio
# from openai import AsyncOpenAI
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, Runner, AsyncOpenAI, set_tracing_disabled

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

async def main():

    agent = Agent(
        name= "basic-agent",
        instructions= "you are helpful assistant",
        model= OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)
    )

    output = await Runner.run(
        agent,
        "who is founder of pakistan"
    )

    print(output.final_output)

if __name__ == "__main__":
    asyncio.run(main())

