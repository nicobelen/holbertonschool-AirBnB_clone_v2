#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.place import Place
from os import getenv

from .review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship('Place', cascade='all, delete', backref='user')
        reviews = relationship('Review', cascade='all, delete', backref='user')
    else:
        @property  # ??
        def Places(self):
            from models.__init__ import storage
            place_dic = storage.all(Place)
            place_list = []
            for place in place_dic.items():
                if place.values()['state.id'] == self.id:
                    place_list.append(place.name)

            return place_list

        @property  # ??
        def Reviews(self):
            from models.__init__ import storage
            review_dic = storage.all(Review)
            review_list = []
            for review in review_dic.items():
                if review.values()['state.id'] == self.id:
                    review_list.append(review.name)

            return review_list
