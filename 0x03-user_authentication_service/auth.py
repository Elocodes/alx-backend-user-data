#!//bin/env python3
"""
hash password
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


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


def _generate_uuid() -> str:
    """ return a str representation of a new id """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ vaildate password against the email """
        try:
            user = self._db.find_user_by(email=email)
            registered_pwd = user.hashed_password
            if user is not None:
                encode_givenpwd = password.encode('utf-8')
                valid_pwd = bcrypt.checkpw(encode_givenpwd, registered_pwd)
                if valid_pwd:
                    return True
        except Exception:
            pass
        return False

    def create_session(self, email: str) -> str:
        """ assign new session id whenever user logs in """
        session_id = _generate_uuid()
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
