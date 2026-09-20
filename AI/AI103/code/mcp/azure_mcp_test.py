import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server = StdioServerParameters(
        command="dotnet",
        args=[
            "azmcp",
            "server",
            "start",
            "--tool",
            "group_list"
        ]
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()
            result = await session.call_tool(
                "group_list",
                {}
            )

            print(result)

            for tool in tools.tools:
                print(f"Tool: {tool.name}")
                print(f"Description: {tool.description}")
                print(f"Schema: {tool.input_schema}")


asyncio.run(main())