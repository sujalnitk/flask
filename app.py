from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world() :
    return "<h1> Hello, World! <h2>"

@app.route("/test")
def test():
    a = 5+6 
    return "this is my function to run app {}".format(a)

@app.route("/test2")
def test2():
    data = request.args.get('x')
    return "this is a data input from my url {}".format(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0")


