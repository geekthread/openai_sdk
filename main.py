"""
Joke-telling agent demo using the OpenAI Agents SDK.

This script creates a simple conversational agent powered by GPT-4o-mini that
tells jokes and tailors its humor to the user's interests. It uses the OpenAI
Agents SDK's `Runner` to execute the agent and `trace` to record a named trace
of the interaction for observability.

Requirements:
    - OPENAI_API_KEY set in a .env file or the environment
    - openai-agents and python-dotenv packages installed

Usage:
    python main.py
"""

import os
from dotenv import load_dotenv
import asyncio
from agents import Agent, Runner, trace

load_dotenv()

# Agent configured to tell jokes and engage users with tailored humor.
agent = Agent(
    name="Test Agent",
    instructions=(
        "Tells jokes to a user and makes them laugh. You can tell any type of joke, but "
        "make sure it's funny! You can also ask the user questions to get to know them "
        "better and tailor your jokes to their interests."
    ),
    model="gpt-4o-mini",
)


async def main():
    """Run the joke agent with a sample prompt and print its response."""
    with trace("Test Trace"):
        result = await Runner.run(agent, "Tell me a joke about Donald Trump.")
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
