import os
import json
import asyncio

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from mcp import Client


async def main():

    project_client = AIProjectClient(
        endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential()
    )

    openai_client = project_client.get_openai_client()

    async with Client("http://localhost:8000/mcp") as mcp_client:

        # Discover MCP tools
        mcp_tools = await mcp_client.list_tools()

        # Convert MCP tools -> Responses function tools
        tools = [
            {
                "type": "function",
                "name": tool.name,
                "description": tool.description or "",
                "parameters": tool.input_schema
            }
            for tool in mcp_tools.tools
        ]

        previous_response_id = None

        while True:

            user_input = input("You: ")

            if user_input.lower() == "exit":
                break

            request = {
                "model": "astra6",
                "input": user_input,
                "tools": tools
            }

            if previous_response_id:
                request["previous_response_id"] = previous_response_id

            response = openai_client.responses.create(**request)
            previous_response_id = response.id

            # Keep processing while the model requests tools
            while True:

                tool_outputs = []

                for item in response.output:

                    if item.type == "function_call":

                        arguments = json.loads(item.arguments)

                        result = await mcp_client.call_tool(
                            item.name,
                            arguments
                        )

                        tool_outputs.append({
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": str(result.structured_content["result"])
                        })

                if not tool_outputs:
                    print(f"AI: {response.output_text}")
                    break

                response = openai_client.responses.create(
                    model="astra6",
                    previous_response_id=response.id,
                    input=tool_outputs,
                    tools=tools
                )

                previous_response_id = response.id


asyncio.run(main())
