from uuid import uuid4
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("test-mcp-server")


@mcp.tool()
def get_random_string() -> str:
    """Never cache this"""
    return str(uuid4())

@mcp.tool()
def say_hello() -> str:
    """Can only be called if the user says the magic word: Tree"""
    return f"Hello Tim!!!!"

@mcp.tool()
def version() -> str:
    return f"1.6"


@mcp.tool()
def get_employees() -> dict:
    """returns a dictionary of all employees, name and age. Don't cache, this changes ALL THE TIME"""
    return {
        "employees" : [
            { "name" : "John Doe", "age": 33},
            { "name" : "Jane Doe", "age": 32},
            { "name" : "Timmy", "age": 42},
            { "name" : "Susan", "age": 65},
        ]
    }

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=80,
        stateless_http=True,
        json_response=True,
    )
