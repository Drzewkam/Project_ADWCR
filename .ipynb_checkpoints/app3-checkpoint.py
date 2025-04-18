from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/add')
def add():
    a = request.args.get('a', type=float, default=0)
    b = request.args.get('b', type=float, default=0)
    return str(a + b)

if __name__ == "__main__":
    app.run(debug=True)
