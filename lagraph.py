import os
import time
import streamlit as st
from langchain_groq import ChatGroq
from graphviz import Digraph
from langgraph.graph import START, END, StateGraph
from langgraph.graph.message import add_messages
from typing import Annotated, TypedDict

# FIXED: Added missing import for ChatGroq

from langchain_core.messages import HumanMessage, BaseMessage

# FIXED: st.set_page_config MUST be the very first Streamlit command executed
st.set_page_config(page_title="langgraph visualization", layout="wide")
st.title("LangGraph Visualization")

API_KEY = ""

# FIXED: Corrected conditional environment setting logic
if API_KEY:
    os.environ["GROQ_API_KEY"] = API_KEY

# FIXED: Annotated uses square brackets []
class State(TypedDict):
    message: Annotated[list[BaseMessage], add_messages]

# Add the LLM
llm = ChatGroq(
    groq_api_key=API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

# Chatbot node
def chatbot_node(state: State):
    # Safely pull the text content of the last message
    last_message = state["message"][-1]
    content = last_message.content if hasattr(last_message, 'content') else str(last_message)
    
    response = llm.invoke([HumanMessage(content=content)])
    # FIXED: Corrected "mesaage" typo to "message"
    return {"message": [response]}

# Build LangGraph workflow
workflow = StateGraph(State)
workflow.add_node("chatbot", chatbot_node)

# FIXED: Replaced faulty add_node connections with proper edges
workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", END)

app = workflow.compile()

# Visualizing function
def draw_graph(active_node=None):
    graph = Digraph()
    
    # FIXED: Ensured variable logic assigns fill colors correctly based on node state
    start_color = "red" if active_node == START else "white"
    bot_color = "green" if active_node == "Chatbot" else "white"
    end_color = "blue" if active_node == END else "white"
    
    graph.node(
        "START",
        style="filled",
        fillcolor=start_color,
        shape="ellipse"
    )
    graph.node(
        "Chatbot",
        style="filled",
        fillcolor=bot_color,  # FIXED: Pointed to bot_color instead of start_color
        shape="box"
    )
    graph.node(
        "END",
        style="filled",
        fillcolor=end_color,
        shape="ellipse"
    )
    
    graph.edge("START", "Chatbot")
    graph.edge("Chatbot", "END")
    return graph

st.subheader("LangGraph Workflow")
graph_placeholder = st.empty()
graph_placeholder.graphviz_chart(draw_graph())

user_input = st.text_input("Enter your message:")

if st.button("Run Workflow"):
    if not user_input.strip():
        st.error("Please enter a valid message before running.")
    else:
        status_text = st.empty()
        status_text.warning("Running workflow...")
        
        # Step 1: START active
        graph_placeholder.graphviz_chart(draw_graph(START))
        time.sleep(1)
        
        # Step 2: Chatbot active
        graph_placeholder.graphviz_chart(draw_graph("Chatbot"))
        
        # Invoke LangGraph
        input_state = {"message": [HumanMessage(content=user_input)]}
        results = app.invoke(input_state)
        time.sleep(1)
        
        # Step 3: END active
        status_text.success("Execution completed!")
        graph_placeholder.graphviz_chart(draw_graph(END))
        
        # FIXED: Extract and display the final message response from state history
        st.subheader("Chatbot Response:")
        final_reply = results["message"][-1].content
        st.write(final_reply)
else:
    st.info("Please enter a message and click 'Run Workflow'")