#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """
    Class that inherits from BaseModel is used
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
