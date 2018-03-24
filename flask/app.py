from flask import Flask
from flask import render_template,jsonify,request
import requests
import os

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat_response():
    rasa_host = os.environ["RASA_HOST"]
    if 'question' in request.args:
        print(request.args['question'])
        user_message = request.args['question']
        print("This is the user message: {}".format(user_message))
        print("The rasa host is: {}".format(rasa_host))
        url = "http://{}:5000/parse".format(rasa_host)
        response = requests.get(url,params={"q":user_message, "project": "chatbot"})
        print(response.json())
        response = response.json()
        print(response)
        intent = response["intent"]
        print("Intent {}".format(intent))
        if intent['name'] == 'help':
            response_text = "Sure I can help you"
        elif intent['name'] == 'greet':
            response_text = "Hello, how may I help?"
        elif intent['name'] == 'goodbye':
            response_text = "Goodbye, have a good day."
        else:
            response_text = "Sorry I don't understand"
        return jsonify({"status": "success", "response": response_text})
    else:
        return jsonify({"status": "failed", "response": "could not find question"})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5005)
