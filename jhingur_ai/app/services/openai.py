import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

def get_completion(prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
