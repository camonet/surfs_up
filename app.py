from flask import Flask
#create a new Flask instance called app:
app = Flask(__name__)
#define startign point of the route
@app.route('/')
def hello_world():
    return 'Hello world'
