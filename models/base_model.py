#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """
    Defines all common attributes/methods for other classes.
    """

    def __init__(self):
        """
        Initialize the BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return the string representation of the BaseModel.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all values of the instance's __dict__.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_t'] = self.created_at.isoformat()
        new_dict['updated_t'] = self.updated_at.isoformat()
        return new_dict
