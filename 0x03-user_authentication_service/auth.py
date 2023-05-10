#!/usr/bin/env python3
"""Auth Module for user service"""

import bcrypt


def _hash_password(password: str) ->str:
    """return hashed password
    """
    if password is None:
        return
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
