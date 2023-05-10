#!/usr/bin/env python3
""" App module """

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def addusers() -> str:
    """register user"""

    user_type = {
        "email": request.form.get('email'),
        "password": request.form.get('password')
    }
    res = Auth.register_user(AUTH, user_type['email'], user_type['password'])
    try:
        return jsonify({"email": res.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ create session id if correct email and password"""
    user_info = {
        "email": request.form.get('email'),
        "password": request.form.get('password')
    }
    if Auth.valid_login(AUTH, user_info['email'], user_info['password']):
        session_id = Auth.create_session(AUTH, user_info['email'])
        res = jsonify({"email": user_info['email'], "message": "logged in"})
        res.set_cookie('session_id', session_id)
        return res
    else:
        abort(401)


if __name__ == "__main__":
    app.run()
