import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def process_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um assistente de vendas de roupas."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
