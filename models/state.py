#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City",
                          backref=backref("state",
                                          cascade="all, delete-orphan"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
