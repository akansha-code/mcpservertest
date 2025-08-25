from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather", host="0.0.0.0", port=8000);

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.
    Args:
        location: location, can be a city, country, state etc.
    """
    return "The Weather is Hot and Dry"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
