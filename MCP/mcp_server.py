from fastmcp import FastMCP

from VectorDatabase import vector_database

mcp=FastMCP("mcp_server")

@mcp.tool
def search(keyword:str):
    return vector_database.query(keyword)

if __name__ == "__main__":
    mcp.run()