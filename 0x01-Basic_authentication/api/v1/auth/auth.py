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
        """ get auth.
        Define routes that dont need authentication. return false for them
        """
        if (path is None) or (excluded_paths is None) or excluded_paths == []:
            return True
        path = path if path.endswith('/') else path + '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ auth header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ get user """
        return None
