import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(page_title="InquisiAI - Research Assistant", page_icon="🔬")
st.title("🔬 InquisiAI: Your Research Assistant")
st.markdown("Ask deep, scholarly questions. InquisiAI synthesizes insights from academic and open web sources.")

# Sidebar
st.sidebar.header("🔐 API Configuration")
api_key = st.sidebar.text_input("Groq API Key", type="password")
research_mode = st.sidebar.checkbox("🎓 Research Mode (Arxiv + Wikipedia only)", value=True)

# Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=2, doc_content_chars_max=300)
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)

arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)
search = DuckDuckGoSearchRun(name="Search")

# Tool selection
tools = [arxiv, wiki] if research_mode else [search, arxiv, wiki]

# Session state for chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi! I'm InquisiAI. Ask me anything scholarly or technical!"}
    ]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Handle user input
if prompt := st.chat_input("Ask a research question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Initialize LLM and agent
    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)

    # Display response
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.markdown(response)
