from flask import Flask
from flask import render_template,jsonify,request
import requests
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
rasa_host = os.getenv("docker_host_ip")

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/chat')
def chat_response():
    if 'question' in request.args:
        print(request.args['question'])
        user_message = request.args['question']
        print("This is the user message: {}".format(user_message))
        print("The rasa host is: {}".format(rasa_host))
        url = "http://{}:5000/parse".format(rasa_host)
        response = requests.get(url,params={"q":user_message, "project": "chatbot"})
        print(response.json())
        response = response.json()
        intent = response["intent"]
        print("Intent {}".format(intent))
        return jsonify({"status": "success", "response": intent})
    else:
        return jsonify({"status": "failed", "response": "could not find question"})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5005)
