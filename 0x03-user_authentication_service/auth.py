#!/usr/bin/env python3
"""Auth Module for user service"""

import bcrypt
from db import DB
from user import User


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
        if self._db.find_user_by(email=email):
            raise ValueError(f"User {email} already exists")
        self._db.add_user(email, _hash_password(password))
        self._db.commit()
        return self._db.find_user_by(email=email)
