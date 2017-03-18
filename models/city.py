#!/usr/bin/python3
from models import *


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)
