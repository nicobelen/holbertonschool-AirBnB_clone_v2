#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from os import getenv

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship('Place', cascade='all, delete', backref='user')
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
