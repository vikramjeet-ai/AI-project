from openai import OpenAI
import os
from dotenv import load_dotenv


model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_career_paths(interests, skills, education):
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4"),
        messages=[
            {"role": "system", "content": "You are a helpful career assistant."},
            {"role": "user", "content": f"My interests: {interests}, skills: {skills}, education: {education}. Suggest best career paths."}
        ]
    )
    return response.choices[0].message.content.strip()

