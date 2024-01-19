#!/usr/bin/env python3
"""
module for user authentication systems
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    class manages the API Authentications
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ get auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ auth header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ get user """
        return None
