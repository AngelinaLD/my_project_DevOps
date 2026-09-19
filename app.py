from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/tasks")
def tasks():
    return jsonify([
        {"id": 1, "title": "Начать делать контрольную точку по Docker", "done": False},
        {"id": 2, "title": "Сдать контрольную точку преподавателю (17 октября последний срок)", "done": False}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)