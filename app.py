from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    """
    Check the strength of a password based on:
    - Length (at least 8 characters)
    - Complexity (uppercase, lowercase, numbers, special characters)
    """
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~`]", password):
        strength += 1
    return strength

@app.route("/check", methods=["POST"])
def check_password():
    """
    Endpoint to check password strength.
    Expects a JSON payload with a "password" field.
    """
    password = request.json.get("password")
    if not password:
        return jsonify({"error": "Password is required"}), 400

    strength = check_password_strength(password)
    if strength <= 2:
        result = "Weak"
    elif strength <= 4:
        result = "Medium"
    else:
        result = "Strong"

    return jsonify({"strength": result})

if __name__ == "__main__":
    app.run(debug=True)
