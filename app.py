from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/compare')
def compare():
    x = request.args.get('x', type=float)
    y = request.args.get('y', type=float)
    if x is None or y is None:
        return jsonify({"error": "Podaj parametry x i y"}), 400

    if x > y:
        decision = "x jest większe od y"
    elif x < y:
        decision = "y jest większe od x"
    else:
        decision = "x jest równe y"

    return jsonify({
        "x": x,
        "y": y,
        "decision": decision
    })

if __name__ == "__main__":
    app.run(debug=True)
