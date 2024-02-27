#!/usr/bin/python3
"""Base model"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Saving datas"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert class infos to dict"""
        new = {
            "my_number": self.__dict__.get("my_number"),
            "name": self.__dict__.get("name"),
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "id": self.id,
            "created_at": self.created_at.isoformat()
        }
        return new

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
