import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = (self.usecase or "").strip().lower()
        graph = self.graph
        user_message = self.user_message

        if usecase == "basic chatbot":
            for event in graph.stream({"messages": ("user", user_message)}):
                for value in event.values():
                    messages = value.get("messages", [])
                    if not messages:
                        continue

                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(getattr(messages, "content", messages))

        elif usecase == "chatbot with web":
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)
            for message in res.get("messages", []):
                if isinstance(message, HumanMessage):
                    with st.chat_message("user"):
                        st.write(message.content)
                elif isinstance(message, ToolMessage):
                    with st.chat_message("assistant"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif isinstance(message, AIMessage) and getattr(
                    message, "content", None
                ):
                    with st.chat_message("assistant"):
                        st.write(message.content)
