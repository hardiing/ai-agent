import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

def main():
    print("Hello from bootdev-llm!")
    #if len(sys.argv[1]) > 3:
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages)
    #else:
        #print("error")
        #sys.exit(1)
    print(response.text)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
