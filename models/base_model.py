#!/usr/bin/python3
"""unittest"""

class BaseModel:
    """BaseModel class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = date_time.now()
        self.updated_at = date_time.now()

    def __str__(self):
        print("[BaseClass] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        updated_at = date_time.now()

    def to_dict(self):

