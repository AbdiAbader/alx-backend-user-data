#!/usr/bin/env python3
"""DB module for a SQLAlchemy database
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """method that return a new user
        """
        newUser = User(email=email, hashed_password=hashed_password)
        self._session.add(newUser)
        self._session.commit()
        return newUser

    def find_user_by(self, **kwargs) -> User:
        """method that return the first row found
        in the users table
        """
        try:
            res = self._session.query(User).filter_by(**kwargs).first()
            if res is None:
                raise NoResultFound
            return res
        except TypeError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """update the database
        """
        res = self.find_user_by(id=user_id)
        if not res:
            raise NoResultFound
        for key, value in kwargs.items():
            if hasattr(res, key):
                setattr(res, key, value)
            else:
                raise ValueError
        self._session.commit()
