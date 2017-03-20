#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class User(BaseModel, Base):
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place",
                          backref=backref("user",
                                          cascade="all, delete-orphan"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
