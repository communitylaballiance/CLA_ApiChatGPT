# open virtual environment = source venv/bin/activate
# turn on the api = python3 main.py

from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
from flask_cors import cross_origin
import openai
import os

app = Flask(__name__)
CORS(app, resources={r"/chatgpt/*": {"origins": "*"}})

def get_chatgpt_response(messages):
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages
    )

    return response['choices'][0]['message']['content']

@app.route('/chatgpt/chat', methods=['POST'])
def getChatResponse():
    messages = request.json['messages']
    print(messages)
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model_response = get_chatgpt_response(messages)
    return {"data": model_response}

@app.route("/chatgpt/corstest", methods=["POST"])
# @cross_origin()
def helloWorld():
  test = request.json['test']
  return {"answer": test}

@app.route('/')
def main():
    return {"test": "Ok"}

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port='3000', debug=True)