import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome, this a sample web application"

@app.route('/try')
def hello():
    return 'Please clone and try the given sample'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
