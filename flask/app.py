from flask import Flask
from flask import render_template,jsonify,request
import requests
app = Flask(__name__)
from dotenv import load_dotenv
load_dotenv()

rasa_host = os.getenv("docker_host_ip")
@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/chat',methods=["POST"])
def chat():
    try:
        user_message = request.form["text"]
        print(user_message)
        response = requests.get("http://10.0.0.218:5000/parse",params={"q":user_message, "project": "chatbot"})
        print(response.json())
        response = response.json()
        intent = response["intent"]
        print("Intent {}".format(intent))
        return jsonify({"status": "success", "response": intent})
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
