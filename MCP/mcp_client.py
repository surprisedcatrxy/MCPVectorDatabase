import asyncio
from fastmcp import FastMCP, Client

from MCP import mcp_server  

client=Client(mcp_server.mcp)

async def call_tool(keyword:str):
    async with client:
        results=await client.call_tool("search",{"keyword":keyword})
        print(f"result is:{results}")

def test(keyword:str):
    asyncio.run(call_tool(keyword))