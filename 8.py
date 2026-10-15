from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "12345"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == USERNAME and password == PASSWORD:
        return jsonify({
            "success": True,
            "message": "Login successful"
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Invalid username or password"
        }), 401


if __name__ == '__main__':
    app.run(debug=True)
