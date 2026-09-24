import asyncio
from mcp import Client

async def main():
    async with Client("https://learn.microsoft.com/api/mcp") as client:

        result = await client.list_tools()

        for tool in result.tools:
            print(tool.name)

asyncio.run(main())
