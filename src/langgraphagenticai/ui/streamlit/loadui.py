import os

import streamlit as st

from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(
            page_title="🤖 " + self.config.get_page_title(), layout="wide"
        )
        st.header("🤖 " + self.config.get_page_title())
        if "timeframe" not in st.session_state:
            st.session_state.timeframe = ""
        if "IsFetchButtonClicked" not in st.session_state:
            st.session_state.IsFetchButtonClicked = False

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Select Model", model_options
                )
                groq_api_key = st.session_state.get(
                    "GROQ_API_KEY", os.getenv("GROQ_API_KEY", "")
                )
                self.user_controls["GROQ_API_KEY"] = st.session_state[
                    "GROQ_API_KEY"
                ] = st.text_input("API Key", type="password", value=groq_api_key)
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning(
                        " ⚠️ Please enter your GROQ API key to proceed. Don't have? refer: https://console.groq.com/keys"
                    )

            # Usecase selection
            previous_usecase = st.session_state.get("selected_usecase")
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecases", usecase_options
            )

            if previous_usecase != self.user_controls["selected_usecase"]:
                st.session_state.IsFetchButtonClicked = False
                st.session_state.timeframe = ""

            if self.user_controls["selected_usecase"] in (
                "Chatbot with Web",
                "AI News",
            ):
                tavily_api_key = st.session_state.get(
                    "TAVILY_API_KEY", os.getenv("TAVILY_API_KEY", "")
                )
                self.user_controls["TAVILY_API_KEY"] = st.session_state[
                    "TAVILY_API_KEY"
                ] = st.text_input(
                    "TAVILIY API Key", type="password", value=tavily_api_key
                )
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning(
                        " ⚠️ Please enter your TAVILIY API Key to proceed. Don't have? refer: https://console.groq.com/keys"
                    )

            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("📰 AI News Explorer ")

                with st.sidebar:
                    time_frame = st.selectbox(
                        "📅 Select Time Frame", ["Daily", "Weekly", "Monthly"], index=0
                    )
                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame

        return self.user_controls
