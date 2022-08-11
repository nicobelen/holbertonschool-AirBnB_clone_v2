#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from os import getenv


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = ""
    user_id = ""
    text = ""
