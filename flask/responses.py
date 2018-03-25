import random

# List of our hello and goodbye responses to pick at random
greeting_response = ["hey", "hello", "hi", "sup"]
goodbye_response = ["have a good one", "goodbye", "bye", "later"]

def greeting():
    return random.choice(greeting_response)

def goodbye():
    return random.choice(goodbye_response)

def about():
    about_response = "Hello I am Lackey AI, a natural language processing bot."
    return about_response
