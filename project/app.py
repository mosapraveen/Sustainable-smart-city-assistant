from flask import Flask, request, jsonify
from ai_engine import ask_assistant

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def handle_query():
    data = request.json
    question = data.get("question", "")
    answer = ask_assistant(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
