#!/usr/bin/env python3
"""Auth Module for user service"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _generate_uuid() -> str:
    """generate uuid"""
    return str(uuid.uuid4())


def _hash_password(password: str) -> str:
    """return hashed password
    """
    if password is None:
        return
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """validte user using checkpw(bcrypt)"""
        try:
            res = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  res.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """create session and return session id"""
        try:
            res = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(res.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """get Users by their session id"""
        try:
            res = self._db.find_user_by(session_id=session_id)
            return res
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroy session"""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Generate a reset tken password if user exists"""
        try:
            res = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(res.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """update password"""
        if password is None:
            return None
        try:
            res = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(res.id, hashed_password=hashed_password,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
