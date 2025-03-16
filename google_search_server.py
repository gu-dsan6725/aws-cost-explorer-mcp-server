"""
Google Search MCP Server.

This server provides MCP tools to perform Google searches and fetch webpage content.
"""

from typing import List
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("google_search")


@mcp.tool()
async def google_search_tool(query: str, num_results: int = 5) -> List[str]:
    """
    Perform a Google search and return the top URLs.
    
    Args:
        query (str): The search query.
        num_results (int): Number of results to fetch.

    Returns:
        List[str]: A list of URLs from Google search.
    """
    try:
        urls = list(search(query, num_results=num_results))
        return urls
    except Exception as e:
        return [f"Error performing Google search: {str(e)}"]


@mcp.tool()
async def fetch_page_text(url: str) -> str:
    """
    Fetch and return the cleaned text content of a webpage.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The extracted and cleaned text content of the page.
    """
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Remove script and style elements
            for tag in soup(["script", "style", "meta", "noscript", "iframe"]):
                tag.decompose()

            # Extract text and clean up extra whitespace
            text = soup.get_text(separator="\n")
            lines = [line.strip() for line in text.splitlines()]
            cleaned_text = "\n".join(line for line in lines if line)  # Remove empty lines

            # Limit response size to prevent overwhelming Claude
            return cleaned_text[:5000] + ("\n[Content truncated]" if len(cleaned_text) > 5000 else "")
        
        return f"Failed to fetch {url}, status code: {response.status_code}"
    
    except Exception as e:
        return f"Error fetching {url}: {e}"


def main():
    """Start the Google Search MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()