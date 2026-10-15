from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

N8N_WEBHOOK_URL = "https://varun5314.app.n8n.cloud/webhook-test/student_data"

@app.route("/student_data", methods=["POST"])
def send_student():
    data = request.get_json()

    response = requests.post(
        N8N_WEBHOOK_URL,
        json=data
    )

    print(response.text)

    return jsonify({
        "success": True,
        "message": "Data sent to n8n successfully",
        "n8n_response": response.text
    })

if __name__ == "__main__":
    app.run(debug=True)