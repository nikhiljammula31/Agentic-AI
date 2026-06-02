#AI Agentic with groq AI Modekl

# pip install groq 
# AI Agentic with Groq API Model
# pip install groq

from groq import Groq

class AIGROQAgent:
    def __init__(self, api_key, model_name="llama-3.3-70b-versatile"):
        self.client = Groq(api_key=api_key)
        self.model_name = model_name

    def generate_response(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are an autonomous AI agent that solves tasks step-by-step in a structured way."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1024,
        )

        return response.choices[0].message.content.strip()

    def execute_task(self, experience_details):
        learning_prompt = f"""
You are an autonomous AI Agent.
analyze th following experience 
and provide insights for improvemeent

Experience
{experience_details}

reflect on this experience and provide insights for improvements.
"""
        return self.generate_response(learning_prompt)


if __name__ == "__main__":
    #API_key = ""  

    agent = AIGROQAgent(API_key)
     # prompt = input("enter your prompt:")
    # response = agent.generate_response(prompt)
    # print("AI responses:",response)
    # prompt1 = "Provide the top 3 bike companies with details"

    # response1 = agent.execute_task(prompt1)

    # print("AI Task response:\n", response1)


    prompt1 = "students enjoyed hands on ai demos but struggled with R lang setup"

    response1 = agent.execute_task(prompt1)

    print("AI learning response:\n", response1)
