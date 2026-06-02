#ollama ai agentic program
#pip install ollama
#ollama run llama3.2
import ollama
convo=[]
def stream_ollama(prompt):
    convo.append({'role':'user','content':prompt})
    response=""
    stream=ollama.chat(model='AI-NIKHIL',messages=convo,stream=True)
    for chunk in stream:
        response+=chunk['message']['content']
        print(chunk['message']['content'],end='',flush=True)
    convo.append({'role':'assistant','content':response})
    
prompt="explain the python OOPS?"
stream_ollama(prompt)

import ollama
from langchain_community.llms import ollama
#create ollama LLM object
ollama_llm = ollama(
    base_url=""
    model="llama3.2"
)
#generate response
response =ollama_llm.invoke("what is python OOPS?")
print(response)

