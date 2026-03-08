# LangGraph Agentic AI Chatbot

This project is an end-to-end agentic AI chatbot built using Python, LangGraph, and Streamlit. It provides a modular framework for creating and running different types of AI agents, from simple conversational bots to complex agents that can use tools and perform autonomous tasks.

## Features

*   **Multi-Agent Architecture**: The application supports multiple, distinct use cases that can be selected from the UI:
    *   **Basic Chatbot**: A standard conversational agent for general queries.
    *   **Chatbot with Tool**: An advanced agent that can use the **Tavily Search** tool to answer questions about real-time events and information.
    *   **AI News**: An autonomous agent that fetches the latest AI news for a given frequency (daily, weekly, monthly), summarizes it, and saves the summary as a markdown file.
*   **Stateful Graphs with LangGraph**: Each agent is built as a stateful graph using LangGraph, allowing for complex, multi-step logic and cycles.
*   **Interactive Web UI**: A clean and user-friendly interface built with Streamlit allows for easy interaction with the agents.
*   **Configurable Backend**: Easily configure the LLM (e.g., Groq), models, and API keys through the sidebar and a simple `.ini` configuration file.

## Getting Started

### Prerequisites

*   Python 3.9+
*   An internet connection
*   API keys for Groq and Tavily

### Installation

1.  **Clone the repository** (if applicable).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt 
    ```
    *(Note: You may need to create a `requirements.txt` file based on your project's libraries if one does not exist.)*

### Running the Application

1.  **Launch the Streamlit app** from your terminal:
    ```bash
    streamlit run app.py
    ```
2.  **Open your web browser** and navigate to the local URL provided by Streamlit (e.g., `http://localhost:8501`).
3.  In the sidebar, select the LLM, enter your **Groq API Key**, choose a use case, and provide the **Tavily API Key** if required.
4.  Start chatting or fetch AI news!
