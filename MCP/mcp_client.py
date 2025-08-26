import asyncio
from fastmcp import FastMCP, Client

from MCP import mcp_server  

client=Client(mcp_server.mcp)

async def call_tool(keyword:str):
    async with client:
        results=await client.call_tool("search",{"keyword":keyword})
        return results
