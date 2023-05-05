#!/usr/bin/env python3
"""BasicAuth class that inherits from Auth"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar, Union
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class that inherits
    from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extracts the Base64"""
        if authorization_header is None or type(authorization_header) is not str:
            return None
        if authorization_header[0:6] != "Basic ":
            return None
        return authorization_header[6:]
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """returns the decoded value"""
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except:
            return None
        
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password"""
        if decoded_base64_authorization_header is None or type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return decoded_base64_authorization_header.split(':', 1)
    
   
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """that returns the User instance based on his email and password"""
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """ that overloads Auth and retrieves the User instance for a request:"""
        header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        user_credentials = self.extract_user_credentials(decoded_header)
        user = self.user_object_from_credentials(user_credentials[0], user_credentials[1])
        return user