#!/usr/bin/env python3
"""
hash password
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
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

    def register_user(self, email: str, password: str) -> User:
        """ register new user """
        try:
            self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
