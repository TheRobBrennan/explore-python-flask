from flask import Flask
from random import randint

# Initialize our app with the name of the module that we're running
app = Flask(__name__)


@app.route('/')
def roll_dice():
    random_number = randint(1, 6)
    return "The dice rolled: {}".format(random_number)
