#!/usr/bin/env python3
"""Auth Module for user service"""

import bcrypt

def _hash_password(passw: str) -> bytes:
    """return hashed password
    """
    if passw is None:
        return
    return bcrypt.hashpw(passw.encode(), bcrypt.gensalt())
