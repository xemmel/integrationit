from mcp.server.mcpserver import MCPServer

mcp = MCPServer("test-mcp-server")

@mcp.tool()
def say_hello(name: str) -> str:
    print(f"Saying hello to {name}")
    return f"Hello {name}"

@mcp.tool()
def get_the_meaning(question: str) -> str:
    return (f"The meaning of {question} is NOTHANG!#!")

@mcp.tool()
def get_the_quote() -> str:
    return (f"The quote is UEAH ")

@mcp.tool()
def get_surname(first_name: str) -> str:
    if first_name.lower() == "morten":
        return "la Cour"
    if first_name.lower() == "clara":
            return "la Cour Fernandes"
    return "N/A"

@mcp.tool()
def crazy_math(a: int, b: int) -> int:
    """Doing wrong additions"""
    print(f"Adding {a} and {b}")
    return (a+b)+1

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        stateless_http=True,
        json_response=True,
    )
