import asyncio
from mcp import Client

async def main():
    async with Client("http://localhost:8000/mcp") as client:

        result = await client.list_tools()

        for tool in result.tools:
            print(tool.name)

        result = await client.call_tool(
            "say_hello",
            {"name": "Morten"}
        )

        print(result)

asyncio.run(main())
