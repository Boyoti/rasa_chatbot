# rasa_chatbot
testing out the rasa chatbot

# To Use
1. Clone the repo - `git clone https://github.com/lackeyai/rasa_chatbot.git`

2. Copy the .env.default file to .env `cp .env.default .env` and put in your Docker IP address or the ip of where docker is installed.

3. Run the following command to bring up rasa and the flask instance - `docker-compose up -d --build --remove-orphans`

4. Verify you can get to the GUI at http://localhost:5005 or whatever IP docker is running at.

5. Test the flask api to ensure it is routing calls to Rasa by calling the below replacing the X.X.X.X with your docker IP:

```python
 import requests
 question = 'can you help me'
 url = 'http://X.X.X.X:5005/chat?question=can you help me'
 r = requests.get(url)
 r.json()
 ```

 This should give you something similiar to the below if you used my training model:

 ```json
 {'response': {'confidence': 0.7104371716052071, 'name': 'help'},
 'status': 'success'}
 ```

# GUI
The chatbot GUI can be accessed at http://localhost:5005/ and interacts with the flask API which then sends the text to Rasa for intent classification and then the bot responds with the appropriate response.

![Screenshot](screenshot.JPG?raw=true)

# Demo
You can demo this at http://chat.btotharye.com:5005/
