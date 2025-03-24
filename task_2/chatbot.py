import os
from dotenv import load_dotenv
from openai import OpenAI
from tools import load_sales_data

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI with OpenRouter base URL
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Load product/sales info
sales_context = load_sales_data()

def ask_chatbot(user_input, context):
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",  # FREE model from OpenRouter
        messages=[
            {"role": "system", "content": f"You are a helpful sales assistant. Here are the available products:\n\n{context}"},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(" Welcome to the Product Chatbot! \nType 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Goodbye!")
            break
        reply = ask_chatbot(user_input, sales_context)
        print("Bot:", reply)
