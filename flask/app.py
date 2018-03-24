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

@app.route('/chat',methods=["POST"])
def chat():
    print(request.form)
    user_message = request.form["text"]
    print("This is the user message: {}".format(user_message))
    print("The rasa host is: {}".format(rasa_host))
    response = requests.get("http://{}:5000/parse",params={"q":user_message, "project": "chatbot"}.format(rasa_host))
    print(response.json())
    response = response.json()
    intent = response["intent"]
    print("Intent {}".format(intent))
    return jsonify({"status": "success", "response": intent})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5005)
