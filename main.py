"""
Joke-telling agent demo using the OpenAI Agents SDK.

This script creates a simple conversational agent powered by GPT-4o-mini that
tells jokes and tailors its humor to the user's interests. It uses the OpenAI
Agents SDK's `Runner` to execute the agent and `trace` to record a named trace
of the interaction for observability.

Key concepts demonstrated:
    - Agent: Defines the LLM-backed assistant with a name, system instructions,
      and a specific model. The instructions act as the system prompt.
    - Runner.run: Asynchronously executes the agent with a user message and
      returns a RunResult whose `.final_output` contains the agent's last reply.
    - trace: A context manager that groups all SDK calls made inside it under a
      named trace, making them visible in the OpenAI dashboard for debugging and
      monitoring.

Requirements:
    - OPENAI_API_KEY set in a .env file or the environment
    - openai-agents and python-dotenv packages installed
      (pip install openai-agents python-dotenv)

Usage:
    python main.py
"""

import asyncio

from agents import Agent, Runner, trace
from dotenv import load_dotenv

# Load OPENAI_API_KEY (and any other vars) from a .env file if present.
# Must be called before the SDK makes any API requests.
load_dotenv()

# ---------------------------------------------------------------------------
# Agent definition
# ---------------------------------------------------------------------------
# The Agent is stateless — it holds only configuration (name, instructions,
# model). Conversation history and execution state are managed by Runner.run.
agent = Agent(
    name="Joke Telling Agent",
    instructions=(
        "Tells jokes to a user and makes them laugh. You can tell any type of joke, but "
        "make sure it's funny! You can also ask the user questions to get to know them "
        "better and tailor your jokes to their interests."
    ),
    model="gpt-4o-mini",  # Cost-efficient model; swap for gpt-4o for higher quality.
)


async def main() -> None:
    """Run the joke agent with a user-supplied subject and print its response.

    The `trace` context manager wraps the run so that all underlying API calls
    are grouped under "Test Trace" in the OpenAI Agents observability dashboard.
    `Runner.run` sends the user message to the agent and returns once the agent
    produces a final response (i.e., it stops calling tools or looping).
    """
    while True:
        subject = input("What would you like to hear a joke about? (type 'quit' or 'bye' to exit) ")
        if subject.strip().lower() in ("quit", "bye"):
            print("Goodbye!")
            break
        with trace("Test Trace"):
            result = await Runner.run(agent, f"Tell me a joke about {subject}.")
            # final_output is the last text message produced by the agent.
            print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
