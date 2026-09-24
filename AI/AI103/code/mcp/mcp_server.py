from mcp.server.mcpserver import MCPServer

mcp = MCPServer("test-mcp-server")

@mcp.tool()
def say_hello(name: str) -> str:
    print(f"Saying hello to {name}")
    return f"Hello {name}"

@mcp.tool()
def crazy_math(a: int, b: int) -> int:
    """Doing wrong additions"""
    print(f"Adding {a} and {b}")
    return 42

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        stateless_http=True,
        json_response=True,
    )
