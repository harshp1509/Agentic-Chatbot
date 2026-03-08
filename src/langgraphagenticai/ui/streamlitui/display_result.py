import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase=usecase
        self.graph=graph
        self.user_message=user_message

    def display_result_on_ui(self):
        usecase=self.usecase
        graph=self.graph
        user_message=self.user_message
        if usecase == "Basic Chatbot":
            for event in graph.stream({"messages":("user",user_message)}):
                print(event.values())
                for value in event.values():
                    # The event value can be None if a node returns nothing.
                    # We must also check for the correct key, "messages", based on the State definition.
                    if not value or "messages" not in value:
                        continue

                    message_payload = value["messages"]
                    # The payload can be a single message object or a list of them.
                    if not isinstance(message_payload, list):
                        message_payload = [message_payload]

                    # Display the user message and then the assistant's response.
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        for msg in message_payload:
                            if hasattr(msg, "content"):
                                st.write(msg.content)

        elif usecase == "Chatbot with Tool":
            initial_state={"messages":[HumanMessage(content=user_message)]}
            res=graph.invoke(initial_state)
            for message in res["messages"]:
                if type(message)==HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message)==ToolMessage:
                    with st.chat_message("assistant"):
                        st.write("Tool call start")
                        st.write(message.content)
                        st.write("Tool call end")
                elif type(message)==AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)

        elif usecase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news..."):
                result=graph.invoke({"messages":frequency})
                try:
                    AI_NEWS_PATH=f"./AINews/{frequency}_summary.md"
                    with open (AI_NEWS_PATH,'r') as file:
                        markdown_content=file.read()
                    st.markdown(markdown_content,unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or file not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"an error occured: {str(e)}")