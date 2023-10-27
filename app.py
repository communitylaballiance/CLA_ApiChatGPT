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
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages
    )

    return response['choices'][0]['message']['content']

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