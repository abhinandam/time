import time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "The number of seconds since January 1st, 1970 is " + str(int(time.time()))

if __name__ == "__main__":
    app.run()
