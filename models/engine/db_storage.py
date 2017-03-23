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

        try:
            if os.environ['HBNB_MYSQL_ENV'] == "test":
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        storage = {}
        if cls is None:
            for cls_name in self.valid_classes:
                for instance in self.__session.query(eval(cls_name)):
                    print(instance)
                    storage[instance.id] = instance
        else:
            if cls not in self.valid_classes:
                return
            for instance in self.__session.query(eval(cls)):
                storage[instance.id] = instance

        self.__session.close()
        return storage

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        try:
            self.__session.commit()
        except:
            self.__session.rollback()
            raise
        finally:
            self.__session.close()

    def update(self, cls, obj_id, key, new_value):
        res = self.__session.query(eval(cls)).filter(eval(cls).id == obj_id)

        print(res.count())

        if res.count() == 0:
            return 0

        res.update({key: (new_value)})
        return 1

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def delete(self, obj=None):
        if obj is None:
            return

        print(obj)
        eval(obj).query.filter_by(id=obj.id).delete()
