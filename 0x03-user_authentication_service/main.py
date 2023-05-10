#!/usr/bin/env python3
""" The Main module"""
from auth import Auth
from user import User

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
Auth = Auth()

def register_user(email: str, password: str) -> None:
    """ register user """
    Auth.register_user(email, password)
    assert Auth.valid_login(email, password) is True

def log_in_wrong_password(email: str, password: str) -> None:
    """ log in with wrong password """
    Auth.register_user(email, password)
    assert Auth.valid_login(email, "wrongpwd") is False

def profile_unlogged() -> None:
    """ profile unlogged """
    user = Auth.register_user(EMAIL, PASSWD)
    assert Auth.create_session(EMAIL) == user.session_id
    assert Auth.get_user_from_session_id(user.session_id) == user.id

def log_in(email: str, password: str) -> str:
    """ log in """
    user = Auth.register_user(email, password)
    assert Auth.create_session(email) == user.session_id
    return user.session_id

def log_out(session_id: str) -> None:
    """ log out """
    user = Auth.get_user_from_session_id(session_id)
    assert user.session_id == session_id
    Auth.destroy_session(user.id)
    assert user.session_id is None

def reset_password_token(email: str) -> str:
    """ reset password token """
    Auth.register_user(email, PASSWD)
    return Auth.get_reset_password_token(email)

def profile_logged(session_id: str) -> None:
    """ profile logged """
    user = Auth.get_user_from_session_id(session_id)
    assert user.session_id == session_id
    assert Auth.create_session(EMAIL) == user.session_id
    assert Auth.get_user_from_session_id(user.session_id) == user.id

def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ update password """
    Auth.register_user(email, PASSWD)
    Auth.update_password(reset_token, new_password)
    assert Auth.valid_login(email, new_password) is True


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)