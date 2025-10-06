from google.adk.agents import Agent
import scalekit.client
import os 

identifier = "user-1234"
connection_name = "gmail"

client = scalekit.client.ScalekitClient(
    client_id=os.getenv("SCALEKIT_CLIENT_ID"),
    client_secret=os.getenv("SCALEKIT_CLIENT_SECRET"),
    env_url=os.getenv("SCALEKIT_ENV_URL",)
)

actions = client.actions




auth = actions.get_authorization_link(identifier=identifier, connection_name=connection_name)

print("📧 Gmail Authorization Required")
print(f"🔗 Visit this URL to authorize the gmail connection:\n\n   {auth.link}\n")
input("✅ Press Enter after authorization...")

gmail_tools = actions.google.get_tools(
    providers=["GMAIL"],
    identifier=identifier,
    page_size=100
)


# Create root agent with all tools
root_agent = Agent(
    name="scalekit_tool_agent",
    model="gemini-2.5-flash",
    description=(
        "You are a tool agent that can work with Gmail and and Answer user questions based in gmail and general questions "
    ),
    instruction=(
        '''
        You are a helpful assistant that can use gmail tools to answer user questions based on their emails and general questions.
        Use the tools to get information from the user's emails and answer their questions.
        Always think step by step and use the tools to get the information you need to answer the user's questions.'''
    ),
    tools=gmail_tools,
)