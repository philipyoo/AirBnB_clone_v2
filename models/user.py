#!/usr/bin/python3
from models import *


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)
