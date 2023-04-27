#!/usr/bin/env python3
""" encrypt_password using bcrypt """

import bcrypt


def hash_password(password: str) -> bytes:
    """hashing password using bcrypt
    and return a salted, hashed password, which is a byte string.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """compares or validated if the hashed password is match the plain password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
