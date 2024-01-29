#!/usr/bin/env python3
"""
set up Flask app
"""

from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ welcome page """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ register a user """
    user_email = request.form.get('email')
    user_pwd = request.form.get('password')
    try:
        AUTH.register_user(user_email, user_pwd)
        return jsonify({"email": user_email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
