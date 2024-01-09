from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'M2I & MQL : Test du Framework  Flask  ! '