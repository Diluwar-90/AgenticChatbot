import os

from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools(tavily_api_key=None):
    """
    Return the list of tools to be used in the chatbot.
    Uses the provided key first, then falls back to the environment.
    """
    api_key = tavily_api_key or os.getenv("TAVILY_API_KEY", "")
    return [TavilySearchResults(max_results=2, tavily_api_key=api_key)]


def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)
