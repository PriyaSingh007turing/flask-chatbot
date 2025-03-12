from flask import Flask, request, jsonify

app = Flask(__name__)

responses = {
    "hello": "Hi! How can I help?",
    "bye": "Goodbye! Have a great day!",
    "help": "I can assist with predefined questions. Try saying 'hello' or 'bye'."
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()
    bot_reply = responses.get(user_message, "Sorry, I don't understand.")
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
