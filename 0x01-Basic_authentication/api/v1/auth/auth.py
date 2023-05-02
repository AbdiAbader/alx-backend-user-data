#!/usr/bin/env python3

""" Auth Module"""

from flask import request
from typing import List, TypeVar


class Auth():
    """class auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        for path in excluded_paths:
            if path.endswith('/') and path[:-1] == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization head"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
