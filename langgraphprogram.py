#graph viz
#diagraph
#pip install graphviz
import streamlit as st
from graphviz import Digraph
def create_graph():
    graph=Digraph()
    graph.node("A","node A")
    graph.node("B","Node B ")
    graph.node("C","node c")
    graph.edge("A","B",label='Edge A-B ')    
    graph.edge("B","C",label='Edge B-C ')
    graph.edge("A","C",label='Edge C-A ')
    return graph
def main():
    st.title("Graph Visualizer with Graphviz")
    graph=create_graph()
    st.graphviz_chart(graph)

if __name__=="__main__":
    main()
