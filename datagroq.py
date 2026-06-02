from groq import Groq
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

api_key=""
client=Groq(
    api_key=api_key
)

text_doc=[
    "AI health care system",
    "AI Education system",
    "AI Finance system",
    "NLP in health care",
    "NLP in education",
]

model=SentenceTransformer('all-miniLM-L6-v2')
doc_embeddings=model.encode(text_doc)
print("embedded Shape : ",doc_embeddings.shape)

d=doc_embeddings.shape[1]
index=faiss.IndexFlatL2(d)
index.add(np.array(doc_embeddings))

query="how is Ai used in healthcare"
query_embedding = model.encode([query])

dist,ids=index.search(np.array(query_embedding),k=2)

context = ""

for inx in ids[0]:
    context+=text_doc[inx]+ "\n"
print("context : ",context)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role" :"system",
            "content" : f"""use this content {context} """
        },
        {
            "role" :"user",
            "content" : query
        }
    ]
)

print("AI Response:")
print(response.choices[0].message.content)
