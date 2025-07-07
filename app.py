import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    message = os.environ.get("WELCOME_MESSAGE", "Hello, World!")
    return f"{message} This is a Flask app deployed via GitHub Actions 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)