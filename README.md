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

### Local development

This sample currently uses a terminal-first authorization flow. That is fine for local development, where you can open the OAuth URL and then press Enter in the same shell after authorization completes.

1. Run the agent. If you are using `uv`, activate your virtual environment first:
   ```bash
   source .venv/bin/activate
   adk run scalekit_tool_agent
   ```

2. Click the Gmail authorization link printed in the terminal, complete authorization, and then press Enter to continue.

<img width="800" height="120" alt="image" src="https://github.com/user-attachments/assets/eaefd372-6030-40ec-9a88-1f1dd8b3f421" />
<br/>
<br/>

3. Start chatting with the agent and ask questions about your emails or general queries.

<img width="368" height="33" alt="image" src="https://github.com/user-attachments/assets/c1e197aa-31f4-43eb-817f-2e502070ed4a" />

### Deploying to the cloud

Do not deploy the current `input()`-based flow unchanged to Railway or other server environments.

The sample prints the OAuth URL and then waits here:

```python
print(f"Visit this URL to authorize: {auth.link}")
input("Press Enter after authorization...")
```

That works in a local terminal, but a deployed process usually has no interactive keyboard input. The app starts, prints the URL, and then waits forever. The deployment can look healthy even though the agent is effectively frozen.

For cloud deployments, use a server-compatible pattern:

1. On each request, call `get_or_create_connected_account(...)`.
2. If `connected_account.status` is not `ACTIVE`, generate an authorization link.
3. Return that link to the user as a normal conversational response and stop the agent for that turn.
4. After the user authorizes access, have them send their message again.
5. Only continue with Gmail-dependent execution after the account is active.

In ADK, the recommended place for this check is `before_agent_callback`, so the first message can return the OAuth URL gracefully instead of blocking the process.

```python
from typing import Optional

from google.adk.agents.callback_context import CallbackContext
from google.genai import types


def ensure_gmail_connection(
    callback_context: CallbackContext,
) -> Optional[types.Content]:
    response = actions.get_or_create_connected_account(
        connection_name=connection_name,
        identifier=identifier,
    )
    connected_account = response.connected_account

    if connected_account.status == "ACTIVE":
        return None

    auth = actions.get_authorization_link(
        identifier=identifier,
        connection_name=connection_name,
    )
    return types.Content(
        role="model",
        parts=[
            types.Part(
                text=(
                    "Authorize Gmail access before I can use Gmail tools: "
                    f"{auth.link}\n\n"
                    "After you finish authorization, send your message again."
                )
            )
        ],
    )
```

Attach that callback to the root agent for deployed environments:

```python
root_agent = Agent(
    name="scalekit_tool_agent",
    model="gemini-2.5-flash",
    description="You are a tool agent that can work with Gmail.",
    instruction="Use Gmail tools to answer questions about the user's email.",
    before_agent_callback=ensure_gmail_connection,
    tools=gmail_tools,
)
```

If your deployment constructs Gmail tools during startup, move that initialization behind the same account-status check or into a request path that runs only after authorization succeeds.

If you keep a separate local-dev flow, reserve `input()` for terminal testing only. For deployed agents, return the authorization link conversationally on the first message and let the user retry once the connected account is active.

## Example Queries
- "Show me my 3 latest emails"
- "What are my unread emails about?"
- "Search for emails from [sender]"
