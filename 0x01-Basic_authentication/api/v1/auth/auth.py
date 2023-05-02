#!/usr/bin/python3

""" Auth Module"""

from flask import request
from typing import List, TypeVar


class Auth():
    """class auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization head"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
