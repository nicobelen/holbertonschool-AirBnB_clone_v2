#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        try:
            if cls is not None:
                with open(FileStorage.__file_path, 'r') as f:
                    temp = {}
                    temp.update(FileStorage.__objects)
                    for key, val in temp.items():
                        if cls == type(val):
                            temp[key] = val
                    return temp
            else:        
                return self.__objects
        except FileNotFoundError:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                if f.read(1) != "":
                    try:  # All good, load json :) --
                        f.seek(0)  # back to pos. 1 of file --
                        temp = json.load(f)
                        for key, val in temp.items():
                            self.all()[key] = classes[val['__class__']](**val)
                        return temp

                    except json.decoder.JSONDecodeError:
                        raise
                else:
                    return {}
                    pass  # File exists, but it's empty --

        except FileNotFoundError:
            return {}
            pass  # File not found --

    def delete(self, obj=None):
        """deletes obj from __objects if it's insida - if obj is equal to
         None, the method should not do anything"""
        if obj is not None:
            try:
                with open(FileStorage.__file_path, 'w') as f:
                    temp = {}
                    temp = self.reload(FileStorage.__objects)
                    #update(FileStorage.__objects)
                    # # esto es inseguro, 
                    # tendriamos que poder reciclar la funcion reload para que 
                    # handlee bien los archivos corruptos y no existentes
                    key = obj.__class__.__name__ + '.' + obj.id
                    if (key in temp.keys()):
                        del temp[key]
                    json.dump(temp, f)
                    self.save()  # esto de alguna forma habria que hacerlo andar
            except Exception:
                pass

