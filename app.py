import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

def retrieve_answer(query):
    logging.info(f"Retrieving answer for query: {query}")
    return f"Dummy answer for: {query}"

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        query = data.get("query")
        
        if not query:
            return jsonify({"error": "Query is required"}), 400
        
        response = retrieve_answer(query)
        return jsonify({"response": response})
    
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)