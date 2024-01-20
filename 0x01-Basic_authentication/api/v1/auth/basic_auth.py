#!/usr/bin/env python3
"""
module contains the basic authentication systems
"""

from api.v1.auth.auth import Auth
import base64
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """ basic authentication class """
    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """
        returns the Base64 part of the Authorization header for a
        Basic Authentication
        """
        auth_header = authorization_header
        if (auth_header is None) or (type(auth_header) is not str):
            return None
        if auth_header.startswith('Basic '):
            return auth_header.split(' ')[1]
        else:
            return None

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        returns the decoded value of a Base64 string
        """
        auth_header = base64_authorization_header
        if (auth_header is None) or (type(auth_header) is not str):
            return None
        try:
            base = base64.b64decode(auth_header)
            return base.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value
        """
        decoded_authH = decoded_base64_authorization_header
        if (decoded_authH is None) or (type(decoded_authH) is not str):
            return (None, None)
        if ':' in decoded_authH:
            email = decoded_authH.split(':')[0]
            password = decoded_authH.split(':')[1]
            return (email, password)
        else:
            return (None, None)

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password.
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users_directory = User.search({'email': user_email})
        except Exception:
            return None
        for user in users_directory:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves users instance of a request"""
        header_auth = request.headers
        if header_auth is None:
            return None
        ext_base = self.extract_base64_authorization_header(header_auth)
        decode_base = self.decode_base64_authorization_header(ext_base)
        user_cred = self.extract_user_credentials(decode_base)
        email = user_cred[0]
        pwd = user_cred[1]
        return self.user_object_from_credentials(email, pwd)
