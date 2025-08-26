import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
API_KEY=os.getenv("API_KEY")

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import Swarm
from autogen_agentchat.conditions import HandoffTermination, TextMentionTermination
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import HandoffMessage

from MCP import mcp_client

# 创建一个简单的模型客户端
model_client = OpenAIChatCompletionClient(
    model="deepseek-chat", 
    api_key=API_KEY,
    base_url="https://api.deepseek.com",
    model_info={
        "family": "unknown",
        "function_calling": True,
        "json_output": False,
        "multiple_system_messages": True,
        "structured_output": True,
        "vision": False,
    },
)

def call_mcp(keyword:str):
    results=asyncio.run(mcp_client.call_tool(keyword))
    return results

query_agent=AssistantAgent(
    "query_agent",
    model_client=model_client,
    handoffs=["user"],
    tools=[call_mcp],
    system_message="""if user say bye or end,Use TERMINATE.
    You can summarize the keywords 
    in the user's questions and must call the tool: call_mcp besides user want to end the chat.
    Combine your cognition and the results of the knowledge base to answer.
    you should answer as briefly as possible.
    If you need information from the user, you must first send your message, then you can handoff to the user.
    when you finish the task,handoff to the user.
    """,
)

termination = HandoffTermination(target="user") | TextMentionTermination("TERMINATE")
team = Swarm([query_agent], termination_condition=termination)

async def run_team_stream(task:str) -> None:
    task_result = await Console(team.run_stream(task=task))
    last_message = task_result.messages[-1]

    while isinstance(last_message, HandoffMessage) and last_message.target == "user":
        user_message = input("User: ")

        task_result = await Console(
            team.run_stream(task=HandoffMessage(source="user", target=last_message.source, content=user_message))
        )
        last_message = task_result.messages[-1]

def run_agent(task:str):
    asyncio.run(run_team_stream(task))
    