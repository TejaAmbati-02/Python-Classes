from flask import Flask
from flask import request
import logging
app = Flask(__name__)
logging.basicConfig(filename="FlaskServerLogs.txt",level = logging.INFO)
@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/hello1")
def hello_world1():
    return "Hello World1"

@app.route("/hello2")
def hello_world2():
    return "Hello World2"

@app.route("/hello3")
def hello_world3():
    return "Hello World3"


@app.route('/test_fun')
def test():
    a = 5+6
    return "This is my first function in flask {}".format(a)


# http://localhost:5000/input_url?data=teja
@app.route('/input_url')
def request_input():
    data = request.args.get('data')
    return "This is my input from url {}".format(data)


if __name__=='__main__':
    app.run(host="0.0.0.0")