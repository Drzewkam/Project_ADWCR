from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/hello/<name>')
def hello(name):
    return f"Cześć, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
