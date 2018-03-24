# rasa_chatbot
testing out the rasa chatbot

# To Use
1. Clone the repo - `git clone https://github.com/lackeyai/rasa_chatbot.git`

2. Modify the .env file and put in your Docker IP address or the ip of where docker is installed.

3. Run the following command to bring up rasa and the flask instance - `docker-compose up -d --build --remove-orphans`

4. Send a curl command to your new Rasa instance to train it, in this example I'm using my own training example hosted on github but this can be any training file you have already created:

`curl 'https://raw.githubusercontent.com/Geeked-Out-Solutions/patreon-rasa-model/master/data/bot-model.json' | curl --request OST --header 'content-type: application/json' -d@- --url '0.0.0.0:5000/train?project=chatbot'` - **Make sure to replace 0.0.0.0 with your docker ip**

5. Test the flask api to ensure it is routing calls to Rasa by calling the below:

`import requests
 question = 'can you help me'
 url = 'http://10.0.0.218:5005/chat?question=can you help me'
 r = requests.get(url)
 r.json()`
 
 This should give you something similiar to the below if you used my training model:
 
 `{'response': {'confidence': 0.7104371716052071, 'name': 'help'},
 'status': 'success'}`

