from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def review_solution(problem, solution):

    prompt = f"""
You are a programming mentor.

Problem:
{problem}

Student Solution:
{solution}

Tasks:

1. Check if solution solves the problem.
2. Find bugs.
3. Suggest improvements.
4. Give a score out of 10.
5. Keep feedback beginner friendly.

Format:

Correctness:
...

Feedback:
...

Improvements:
...

Score:
...
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content