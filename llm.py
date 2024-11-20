import os
from openai import OpenAI

MODEL_NAME = "gpt-4o-2024-05-13"

client = OpenAI()

def get_completion(userContent): 

    response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    { 
                        "role": "system", 
                        "content": "Du är en hjälpful assistent som svarar på svenska" },
                    {
                        "role": "user",
                        "content": userContent,
                    },
                ],                    
            ) 
    return response.choices[0].message.content