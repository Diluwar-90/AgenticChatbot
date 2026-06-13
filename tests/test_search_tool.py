import pytest

from src.langgraphagenticai.tools.search_tool import get_tools


def test_get_tools_raises_when_tavily_key_missing(monkeypatch):
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)

    with pytest.raises(ValueError, match="TAVILY_API_KEY"):
        get_tools("")
