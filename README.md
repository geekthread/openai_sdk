# openai-sdk

A minimal demo of the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) that runs a joke-telling agent powered by GPT-4o-mini.

## What it does

Creates an `Agent` that tells jokes and tailors its humor to the user's interests. At runtime it prompts you for a subject, tells a joke, then loops back to ask again. Type `quit` or `bye` to exit. Each interaction is wrapped in a named `trace` for observability.

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

You will be prompted to enter a subject after each joke. The loop continues until you type `quit` or `bye`:

```
What would you like to hear a joke about? (type 'quit' or 'bye' to exit) cats
<agent tells a joke>
What would you like to hear a joke about? (type 'quit' or 'bye' to exit) bye
Goodbye!
```

## Dependencies

| Package | Version |
|---|---|
| `openai-agents` | >= 0.1.0 |
| `asyncio` | >= 4.0.0 |
| `python-dotenv` | >= 0.9.9 |
