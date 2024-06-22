# open virtual environment = source venv/bin/activate
# turn on the api = python3 main.py

from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def get_chatgpt_response(messages):
    # Call the chat completion endpoint
    response = openai.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo-0125",
    )
    response_message = response.choices[0].message.content
    return response_message

@app.route("/chatgpt/chat", methods=["POST"])
def getChatResponse():
    messages = request.json['messages']
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model_response = get_chatgpt_response(messages)
    print(model_response)
    return {"data": model_response}

@app.route('/')
def main():
    return {"api_test": "Ok"}






