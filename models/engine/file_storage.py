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
        if cls is not None:
            print('CLS NOT NONE')
            temp = dict()
            for key in self.__objects:
                _class = key.split(".")[0]
                print('RECORRIENDO __OBJECTS')
                if cls == _class:
                    print('CLS IN __OBJECTS')
                    print(self.__objects[key])
                    temp[key] = self.__objects[key]
            return temp
        else:
            return self.__objects
            # try:
            #     if cls is not None:
            #         with open(FileStorage.__file_path, 'r') as f:
            #             temp = {}
            #             temp.update(FileStorage.__objects)
            #             for key, val in temp.items():
            #                 if cls == type(val):
            #                     temp[key] = val
            #             return temp
            #     return self.__objects
            # except Exception:
            #     return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            return f.write(json.dumps(self.__objects, default=str))
        # with open(FileStorage.__file_path, 'w') as f:
        #     temp = {}
        #     temp.update(FileStorage.__objects)
        #     for key, val in temp.items():
        #         temp[key] = val.to_dict()
        #     json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                if f.read(1) != "":
                    f.seek(0)
                    self.__objects = json.loads(f.read())
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            raise

    def delete(self, obj=None):
        """deletes obj from __objects if it's insida - if obj is equal to
         None, the method should not do anything"""
        if obj is not None:
            for key, value in self.__objects.items():
                if obj == value:
                    pass
            self.__objects.pop(key)
        # if obj is not None:
        #     if obj in self.__objects.values():
        #         with open(FileStorage.__file_path, 'w') as f:
        #             temp = {}
        #             temp = self.reload(FileStorage.__objects)
        #             #update(FileStorage.__objects)
        #             # # esto es inseguro, 
        #             # tendriamos que poder reciclar la funcion reload para que 
        #             # handlee bien los archivos corruptos y no existentes
        #             key = obj.__class__.__name__ + '.' + obj.id
        #             if (key in temp.keys()):
        #                 del temp[key]
        #                 print('Hasta aca, FLAMA --')
        #             json.dump(temp, f)
        #             self.save()  # esto de alguna forma habria que hacerlo andar

