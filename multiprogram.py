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
plannerAgent=Agent(
    role="Event Planner",
    goal="Plan a birthday party for a 18yr old child",
    backstory="You are an experienced event planner specializing in children",
    verbose=True,
    llm=llm
)
event_name="Super hero birthday bash"
guests=200
date="2026-2-2"
budget=5000
venue="local community center"

planningTask1=Task(
    description=f"""
Plan event :{event_name}
Guests:{guests}
Date:{date}
Venue:{venue}
budget:{budget}
Give:
1.Theme suggestion
2.Activity ideas
3.Food recomnedation
4.Venue decoration ideas
    """,
    expected_output="A event planner is created using AI agents",
    agent=plannerAgent
)
Budgetagent = Agent(
    role="Budget Manager",
    goal="Track expenses, optimize costs, and ensure the entire event stays under budget.",
    backstory="You are an expert financial planner who specializes in event budgeting and maximizing value.",
    verbose=True,
    llm=llm
)


btasks = Task(
    description=f"""
    Check if budget is sufficient for the planned event and provide recommendation
    1. Create a detailed budget breakdown for the event
    2. Track expenses and ensures that all costs are within the budget
    3. Provide recommendation for cost saving measures.
    """,
    expected_output="Detailed budget planner is created",
    agent=Budgetagent
)

riskAgent3=Agent(
    role="risk manager",
    goal="find the possible problems in the event",
    backstory="expert in finding the problems and giving relavent solutions to solve the problem",
    verbose=True,
    llm=llm
)

risktask3=Task(
    description=f"""
Analyze event task:
identify potential problems risks and find possible way to solve it
1.Assess every details in the event like transport parking etcc..
2,Eveluate the safety measures
3.wheater report if the event is outside
4.Crowd management
5.Food storage
6.provide recomdation
""",
expected_output="Risk managment is done using ai agent",
agent=riskAgent3
)

#crew pipeline
crew = Crew(
    agents=[plannerAgent,Budgetagent],
    tasks=[planningTask1,btasks],
    process=Process.sequential,
    verbose=True
)
#RUN THE CREW
results=crew.kickoff()
print("crew compiled.Results:")
print(results)









