from mcp.server.mcpserver import MCPServer

mcp = MCPServer("test-mcp-server")

@mcp.tool()
def say_hello() -> str:
    """Can only be called if the user says the magic word: Tree"""
    return f"Hello Tim!!!!"

@mcp.tool()
def version() -> str:
    return f"1.3"


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=80,
        stateless_http=True,
        json_response=True,
    )
