#!/usr/bin/env python3
""" Task-0 a SQLAlchemy model
named User for a database table named users"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """user class inherits from Base"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
