# openai-sdk

A minimal demo of the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) that runs a joke-telling agent powered by GPT-4o-mini.

## What it does

Creates an `Agent` that tells jokes and tailors its humor to the user's interests, then runs it against a sample prompt using `Runner.run`. The interaction is wrapped in a named `trace` for observability.

## Requirements

- Python >= 3.14
- An OpenAI API key

## Setup

1. Clone the repo and install dependencies with [uv](https://github.com/astral-sh/uv):

   ```bash
   uv sync
   ```

2. Create a `.env` file in the project root with your OpenAI API key:

   ```env
   OPENAI_API_KEY=sk-...
   ```

## Usage

```bash
uv run python main.py
```

The agent's response will be printed to stdout.

## Dependencies

| Package | Version |
|---|---|
| `openai-agents` | >= 0.1.0 |
| `asyncio` | >= 4.0.0 |
| `python-dotenv` | >= 0.9.9 |
