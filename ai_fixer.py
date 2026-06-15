from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_fix(code, errors):

    prompt = f"""
You are an expert Python debugger.

Your goal is to produce the MOST LIKELY fix, not just any fix.

Code:
{code}

Detected Errors:
{errors}

Rules:
1. Make the smallest possible change.
2. Preserve the original intent of the code.
3. Reuse existing variables whenever possible.
4. Do NOT invent new variables, functions, or values unless absolutely necessary.

Return your answer in this format:

Error Explanation:
<explanation>

Corrected Code:
<fixed code>

Why This Fix Works:
<explanation>
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
        {
            "role": "system",
            "content": "You are a senior Python debugger."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.1
)

    return response.choices[0].message.content