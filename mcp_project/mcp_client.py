import asyncio
from pathlib import Path
from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport


async def main():
    server_path = Path(__file__).parent / "mcp_server.py"

    transport = PythonStdioTransport(
        script_path=server_path
    )

    mcp_client = Client(transport)

    async with mcp_client:

        # Get available tools
        tools = await mcp_client.list_tools()

        print("Available tools:")
        for tool in tools:
            print(tool.name)

        # Call add_numbers
        result = await mcp_client.call_tool(
            "add_numbers",
            {
                "a": 10,
                "b": 20
            }
        )

        print("\nAdd result:")
        print(result)

        # Call check_stock
        result = await mcp_client.call_tool(
            "check_stock",
            {
                "item": "apple"
            }
        )

        print("\nStock result:")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())