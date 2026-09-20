import os
import json
import asyncio

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    # ----- Foundry -----

    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]

    credential = DefaultAzureCredential()

    project_client = AIProjectClient(
        endpoint=project_endpoint,
        credential=credential
    )

    openai_client = project_client.get_openai_client()

    # ----- Azure MCP -----

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

            # Discover tools from MCP
            mcp_tools = await session.list_tools()

            # Convert MCP tools -> Responses function tools
            tools = []

            for tool in mcp_tools.tools:

                tools.append({
                    "type": "function",
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.input_schema
                })

            print("MCP tools:", [tool["name"] for tool in tools])

            # ----- Ask the model -----

            user_input = input("Input: ")

            response = openai_client.responses.create(
                model="astra6",
                input=user_input,
                tools=tools
            )

            # ----- Handle tool requests -----

            tool_outputs = []

            for item in response.output:

                if item.type == "function_call":

                    arguments = json.loads(item.arguments)

                    print(
                        f"Model wants MCP tool: {item.name} "
                        f"arguments: {arguments}"
                    )

                    result = await session.call_tool(
                        item.name,
                        arguments
                    )

                    # MCP result -> plain text for Responses
                    output = "\n".join(
                        content.text
                        for content in result.content
                        if content.type == "text"
                    )

                    tool_outputs.append({
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": output
                    })

            # ----- Send MCP results back to model -----

            if tool_outputs:

                response = openai_client.responses.create(
                    model="astra6",
                    previous_response_id=response.id,
                    input=tool_outputs,
                    tools=tools
                )

            print()
            print(response.output_text)


asyncio.run(main())