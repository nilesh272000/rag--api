from flask import Flask, request, jsonify

app = Flask(__name__)

def retrieve_answer(query):
    return f"Dummy answer for: {query}"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query")
    response = retrieve_answer(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)