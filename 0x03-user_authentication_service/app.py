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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """destory user session"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def prof() -> str:
    """find the profile"""
    s_id = request.cookies.get('session_id')
    res = Auth.get_user_from_session_id(AUTH, s_id)
    if res:
        return jsonify({"email": res.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def reset_pass() -> str:
    """checks email and return reset token"""
    email = request.form.get('email')
    try:
        res = AUTH._db.find_user_by(email=email)
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": res.email, "reset_token": token}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """update password if token is valid
    or return 403 if not valid"""
    user_info = {
        "email": request.form.get('email'),
        "reset_token": request.form.get('reset_token'),
        "new_password": request.form.get('new_password')
    }
    try:
        AUTH.update_password(user_info['reset_token'],
                             user_info['new_password'])
        return jsonify({"email": user_info['email'],
                        "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run()
