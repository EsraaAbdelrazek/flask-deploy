from flask inport Flask 
app = flask (__name__)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, swimmer!</p>"
if __name__ =="__main__":
    app.run()
