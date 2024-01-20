#!/usr/bin/env python3
"""
module contains the basic authentication systems
"""

from api.v1.auth.auth import Auth


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
