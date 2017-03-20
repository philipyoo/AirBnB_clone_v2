#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    places = relationship("Place", secondary="place_amenity", viewonly=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
