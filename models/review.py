#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    __tablename__ = "reviews"
    place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
