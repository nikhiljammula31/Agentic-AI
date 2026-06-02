#create wtih multi agent with llm
#pip install crewai
import os
from crewai import Agent,Task,Crew,LLM,Process
from groq import Groq
#set GEMINI_API_KEY="AIzaSyA47D6tUUz8UY3a-SnSm8rdzMdiliX3F-Q" 
os.environ["groq_API_KEY"]=""
#GEMINI AI AGENT
llm=LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.4
)
#user input for the task
#Agent I Event planner 
analyzerAgent=Agent(
    role="Analyzer",
    goal="Analyze the text given by user",
    backstory="You are an experienced agent in analysing the content given by user",
    verbose=True,
    llm=llm
)
analyze_name="Current affairs in india"


anaTask1=Task(
    description=f"""
Plan event :{analyze_name}
Give:
1.The current affairs in india
2.What are the causes for them
3.your idea on it
4.how to reduce them if they are bad
    """,
    expected_output="A Analyser is created using AI agents",
    agent=analyzerAgent
)
reviewagent = Agent(
    role="Reviewer",
    goal="Give your review on the content given by user",
    backstory="You are an expert in giving reviews to the content provided",
    verbose=True,
    llm=llm
)


rtasks = Task(
    description=f"""
    Detailed summary for the content
    1. your opinion on those reviews
    2. Final conclusion about the society
    """,
    expected_output="Review system is created",
    agent=reviewagent
)

solAgent3=Agent(
    role="Solution Finder",
    goal="find the possible solutions for the problems in the current affers",
    backstory="expert in finding the problems and giving relavent solutions to solve the problem",
    verbose=True,
    llm=llm
)

soltask3=Task(
    description=f"""
Analyze current affairs problems:
identify potential problems risks and find possible way to solve it
1.Assess every details in the currebt affairs like politics or any serious investigations etc..
2,Eveluate the safety measures
3.Food storage
4.provide recomdation
""",
expected_output="Solutions are found using ai agent",
agent=solAgent3
)

#crew pipeline
crew = Crew(
    agents=[analyzerAgent,reviewagent,solAgent3],
    tasks=[anaTask1,rtasks,soltask3],
    process=Process.sequential,
    verbose=True
)
#RUN THE CREW
results=crew.kickoff()
print("crew compiled.Results:")
print(results)









