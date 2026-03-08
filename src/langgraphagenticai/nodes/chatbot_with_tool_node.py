from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    def __init__(self,model):
        self.llm=model
    
    def create_chatbot(self,tools):
        """
        Returns a chatbot node function that binds tools to the LLM.
        """
        llm_with_tools = self.llm.bind_tools(tools=tools)
        
        def chatbot_node(state:State):
            """
            Chatbot logic for processing the input state. The response may be a direct
            answer or a tool call.
            """
            response = llm_with_tools.invoke(state["messages"])
            return {"messages": [response]}
        
        return chatbot_node