#!/usr/bin/env python3
""" encrypt_password using bcrypt """

import bcrypt


def hash_password(pw: str) -> bytes:
    """hashing password using bcrypt
    and return a salted, hashed password, which is a byte string.
    """
    return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
