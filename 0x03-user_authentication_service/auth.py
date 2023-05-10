#!/usr/bin/env python3
"""Auth Module for user service"""

import bcrypt


def _hash_password(passw: str) ->str:
    """return hashed password using bcrypt
    and utf-8 encoding
    """
    if passw is None:
        return
    return bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
