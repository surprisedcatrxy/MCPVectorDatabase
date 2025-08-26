import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
API_KEY=os.getenv("API_KEY")

#µº»ÎfastMCP
from MCP import mcp_client

#mcp_client.test("sad")