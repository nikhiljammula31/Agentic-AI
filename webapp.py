#pip install gradio
#pip install groq

import gradio as gr
from groq import Groq 

api_key=""

Client=Groq(api_key=api_key)

#gradio and groq ai based multy pages websites generator application

def generate_function(prompt):
    try:
        response=Client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role" : "system",
                "content" : """
                    You are a seniour web developer  UI/UX Designer and Frontend developer in creating modern websites
                    using javascript,HTML,CSS etc...
                    the website should be visually appealing , user-friendly and responsive across different devices
                    Generate a complete Mlti-page website in ine html file
                    Using internal navigation system
                    Rules :
                    - must be full html document (doctype,STYLES,DIV TAGES,script,body, etc......)
                """
            },
            {
                "role":"user",
                "content": f"""
                    create a profeesional multi-page website for a start up based on the 
                    following {prompt}
                    make it modern,beautiful,responseive for images and ensure content is relative
 """
            }],
            temperature=0.8
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"error :{e}")
        return f"<h2 style='color : red;'>An error occured{str(e)} </h2>"
    
app=gr.Blocks(title="Multi-page website")
with app:
    gr.Markdown("Multi-page website") 
    gr.Markdown("Generate full website with multiple sections")
    prompt= gr.Textbox(
        label="enter a prompt",
        placeholder="a tech startup that provides Ai solutions",
        lines=4
    )   
    btn=gr.Button("Generate Website")
    output=gr.HTML()
    btn.click(
        fn=generate_function,
        inputs=prompt,
        outputs=output,
    )
app.launch(share=True)

