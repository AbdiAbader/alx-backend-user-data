#!/usr/bin/env python3
""" encrypt_password using bcrypt """

import bcrypt


def hash_password(password: str) -> bytes:
    """hashing password using bcrypt
    and return a salted, hashed password, which is a byte string.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
