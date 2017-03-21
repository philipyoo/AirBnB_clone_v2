#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
