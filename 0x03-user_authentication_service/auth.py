#!/usr/bin/env python3
"""Auth Module for user service"""

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """ Takes in string arg, converts to unicode
    Returns salted, hashed pswd as bytestring
    """
    return hashpw(password.encode('utf-8'), gensalt())