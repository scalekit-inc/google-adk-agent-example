# Google ADK Tool Calling Agent

A conversational Google ADK agent powered by Gemini 2.5 Flash with Scalekit integration that demonstrates tool calling capabilities.
This project serves as a foundation for building Google ADK agents with real API integrations.

## Features

- **Gemini 2.5 Flash Agent**: Uses Google's Gemini 2.5 Flash for intelligent conversations and tool selection
- **Scalekit Tools**: Integrated tools for various services (Gmail, etc.)
- **Interactive Chat**: Command-line interface for natural conversations
- **OAuth Authorization**: Secure authorization flow for connected services

## Prerequisites

**Required**: You need both Google API and Scalekit credentials.

1. **Google API Key**: Get from [Google AI Studio](https://aistudio.google.com/apikey)
2. **Scalekit Credentials**: Get from your Scalekit dashboard at [app.scalekit.com](https://app.scalekit.com)
   - Navigate to Developers → Settings → API Credentials
3. Ensure you have access to Gemini API

## Installation

1. Clone or download this project
2. Install dependencies using uv:
   ```bash
   uv sync
   ```
   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   ```bash
   cp scalekit_tool_agent/.env.example scalekit_tool_agent/.env
   # Edit scalekit_tool_agent/.env and add your credentials
   ```

## Configuration

Create a `scalekit_tool_agent/.env` file with the following variables:

```bash
# Google Configuration
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key_here

# Scalekit Configuration
SCALEKIT_CLIENT_ID=your_scalekit_client_id
SCALEKIT_CLIENT_SECRET=your_scalekit_client_secret
SCALEKIT_ENV_URL=your_scalekit_environment_url
```

Get your Scalekit credentials from your dashboard at [app.scalekit.com](https://app.scalekit.com):
- Navigate to Developers → Settings → API Credentials

## Usage

1. Run the agent:
   ```bash
   adk run scalekit_tool_agent
   ```

2. Follow the authorization prompts for each service (e.g., Gmail)
3. Start chatting with the agent and ask questions about your emails or general queries

## Example Queries

- "Show me my recent emails"
- "What are my unread emails about?"
- "Search for emails from [sender]"
- "Summarize my inbox"

## Project Structure

```
google-adk-agent-example/
├── scalekit_tool_agent/
│   ├── __init__.py
│   ├── agent.py          # Main agent implementation
│   └── .env              # Environment variables (gitignored)
├── pyproject.toml        # Project dependencies
├── uv.lock              # Dependency lock file
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Tech Stack

- **Google ADK**: Agent framework for building conversational AI
- **Gemini 2.5 Flash**: Google's latest language model
- **Scalekit SDK**: OAuth and integration management
- **Python 3.11+**: Required Python version

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License
