#!/usr/bin/python3
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import *


class DBStorage:
    __engine = None
    __session = None
    valid_classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://" +
                                      os.environ['HBNB_MYSQL_USER'] +
                                      ":" + os.environ['HBNB_MYSQL_PWD'] +
                                      "@" + os.environ['HBNB_MYSQL_HOST'] +
                                      ":3306/" +
                                      os.environ['HBNB_MYSQL_DB'])

    def all(self, cls=None):
        storage = {}
        if cls is None:
            for instance in self.__session.query(User, State, City,
                                                 Amenity, Place, Review):
                storage[instance.id] = instance
        else:
            if cls not in valid_classes:
                raise TypeError("Invalid class type")
            for instance in self.__session.query(cls):
                storage[instance.id] = instance

        return storage

    def new(self, obj):
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        self.__session.flush()

    def reload(self):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def delete(self, obj=None):
        if obj is None:
            return

        if obj.__class__.__name__ not in valid_classes:
            return

        eval(obj.__class__.__name__).query.filter_by(id=obj.id).delete()
        self.__session.commit()