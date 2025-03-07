import os
import openai
from dotenv import load_dotenv

from prompt import PROMPT

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.base_url = os.getenv("OPENAI_BASE_URL")

client = openai.OpenAI()

def main():
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_CHAT_MODEL"),
        messages=[{"role": "user", "content": PROMPT}]
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
