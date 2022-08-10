#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.orm import Session

user = getenv('HBNB_MYSQL_USER')
passwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_enginge('mysql+mysqldb://\
                                       {user}:{passwd}\
                                       @{host}/{db}',
                                       pool_pre_ping=True)

        self.__session = Session(bind=engine)
    if getenv('HBNB_ENV') == 'test':
        # drop all tables
        pass

    def all(self, cls=None):
        query = session.query(cls).all()
