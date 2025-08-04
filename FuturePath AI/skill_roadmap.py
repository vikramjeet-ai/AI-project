import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_skill_roadmap(career):
    prompt = f"""Create a complete skill roadmap to become a successful {career}.
Include beginner to advanced steps, tools, courses, and milestones."""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a career mentor and learning path expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
