#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
# user = getenv('HBNB_MYSQL_USER')
# passwd = getenv('HBNB_MYSQL_PWD')
# host = getenv('HBNB_MYSQL_HOST')
# db = getenv('HBNB_MYSQL_DB')


class DBStorage():
    __engine = None
    __session = None
    classes = {'State' : State, 'City' : City, 'User' : User, 'Review' : Review, 'Place' : Place}


    def __init__(self):

        if getenv('HBNB_ENV') == 'test':
            pass

    def all(self, cls=None):
        if cls is not None:
            req_class = self.classes[cls]
            query = self.__session.query(req_class).all()
        else:
            query = self.__session.query(cls).all()

        query_dict = {}
        for key in query:
            # _class = query.split(".")[0]
            if cls in self.classes:
                query_dict[key] = key
        return query_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj):
        try:
            del_query = self.__session.query(obj.__class__).all()
            if obj in del_query:
                self.__session.delete(obj)  
        except Exception:
            raise

    def reload(self):
        user = 'hbnb_dev'
        passwd = 'hbnb_dev_pwd'
        host = 'localhost'
        db = 'hbnb_dev_db'
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}/{db}',
                                pool_pre_ping=True)
        #session_factory = sessionmaker(self.__engine, expire_on_commit=False)
        #self.__session = scoped_session(session_factory)
        self.__session = Session(bind=self.__engine)
        Base.metadata.create_all(self.__engine)
        
