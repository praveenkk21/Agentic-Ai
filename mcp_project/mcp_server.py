from fastmcp import FastMCP

# Create MCP server
mcp_server = FastMCP("My MCP Server")


# Tool 1: Add two numbers
@mcp_server.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# Tool 2: Get stock information
STOCK = {
    "apple": 100,
    "banana": 50,
    "orange": 75
}


@mcp_server.tool
def check_stock(item: str) -> str:
    """Check how many units of an item are available in the warehouse."""

    count = STOCK.get(item.lower())

    if count is None:
        return f"{item} is not in the catalogue."

    return f"{count} units of {item} are in stock."


# Start MCP server
if __name__ == "__main__":
    mcp_server.run()