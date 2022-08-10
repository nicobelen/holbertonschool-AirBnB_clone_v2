#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', back_populates='state')
    else:
        @property  # ??
        def cities(self):
            from models.__init__ import storage
            city_dic = storage.all(City)
            city_list = []
            for city in city_dic.items():
                if city.values()['state.id'] == self.id:
                    city_list.append(city.name)

            return city_list
