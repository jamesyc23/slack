from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get('name')
    return 'Hello, World!' + name

app.run()
