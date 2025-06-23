import os
from dotenv import load_dotenv
from agents.run import RunConfig
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",   
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

agent = Agent(
    name="Assistant",
    instructions="you are helpfull assistant",
)

result= Runner.run_sync(
    agent,
    "what is the capital of spain",
    run_config=config
)

print(result.final_output)