import asyncio
import argparse
from mcp import Client

parser = argparse.ArgumentParser()
parser.add_argument("--server")
args = parser.parse_args()

async def main():
    async with Client(args.server) as client:

        result = await client.list_tools()

        for tool in result.tools:
            print(tool.name)

asyncio.run(main())
