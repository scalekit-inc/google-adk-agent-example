# Google ADK Tool Calling Agent

A conversational Google ADK agent powered by Gemini 2.5 Flash with Scalekit integration that demonstrates tool calling capabilities.
This project serves as a foundation for building Google ADK agents with real API integrations.



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
   ```
Edit scalekit_tool_agent/.env and add your credentials

## Configuration

Create a `scalekit_tool_agent/.env` file with the following variables:
Get your Scalekit credentials from your dashboard at [app.scalekit.com](https://app.scalekit.com):
- Navigate to Developers → Settings → API Credentials

```bash
# Google Configuration
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key_here

# Scalekit Configuration
SCALEKIT_CLIENT_ID=your_scalekit_client_id
SCALEKIT_CLIENT_SECRET=your_scalekit_client_secret
SCALEKIT_ENV_URL=your_scalekit_environment_url
```



## Usage

1.<b> Run the agent:</b>
if you are using uv activate you venv `source .venv/bin/activate`
   ```bash
   adk run scalekit_tool_agent
   ```

2. <b>Click on the authorization link for the Gmail and press Enter to continue</b>

<img width="800" height="120" alt="image" src="https://github.com/user-attachments/assets/eaefd372-6030-40ec-9a88-1f1dd8b3f421" />
<br/>
<br/>

3. <b> Start chatting with the agent and ask questions about your emails or general queries</b>

<img width="368" height="33" alt="image" src="https://github.com/user-attachments/assets/c1e197aa-31f4-43eb-817f-2e502070ed4a" />

## Example Queries
- "Show me my 3 latest emails"
- "What are my unread emails about?"
- "Search for emails from [sender]"
