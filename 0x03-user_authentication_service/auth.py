#!/usr/bin/env python3
"""
hash password
"""

import bcrypt
from db import DB


def _hash_password(password):
    """ method takes in a password string, hashes it,
    and returns bytes
    """
    # converting password to array of bytes
    bytess = password.encode('utf-8')
    # generate pseudorandom string that is added to password for added strengt
    salt = bcrypt.gensalt()
    # hash
    hashh = bcrypt.hashpw(bytess, salt)
    return hashh


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ init """
        self._db = DB()
