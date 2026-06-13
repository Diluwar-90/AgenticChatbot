from langchain_core.messages import AIMessage, HumanMessage

from src.langgraphagenticai.ui.streamlit.display_result import DisplayResultStreamlit


class FakeChatMessage:
    def __init__(self, role):
        self.role = role

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class FakeStreamlit:
    def __init__(self):
        self.messages = []

    def chat_message(self, role):
        self.messages.append(role)
        return FakeChatMessage(role)

    def write(self, value):
        self.messages.append(value)


class FakeGraph:
    def __init__(self):
        self.invoked = False

    def invoke(self, state):
        self.invoked = True
        return {"messages": [HumanMessage(content="hello"), AIMessage(content="reply")]}


def test_display_result_handles_chatbot_with_web_case(monkeypatch):
    fake_st = FakeStreamlit()
    monkeypatch.setattr(
        "src.langgraphagenticai.ui.streamlit.display_result.st", fake_st, raising=False
    )

    graph = FakeGraph()
    DisplayResultStreamlit("Chatbot with Web", graph, "hello").display_result_on_ui()

    assert graph.invoked is True
