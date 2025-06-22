import openai
from ..config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_insight(context_lines):
    context = "\n".join(context_lines)
    prompt = f"""
You are a strategic business advisor. Based on the conversation so far:

{context}

Respond with a brief, helpful insight or question to move the discussion forward.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()
