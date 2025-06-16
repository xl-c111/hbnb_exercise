import uuid
from datetime import datetime
from app.models.user import User
from app.models.place import Place


class Review:
    def __init__(self, text, rating, place, user):
        # check in __init__ ensures all required arguments are provided(prevent None but not prevent text=""(empty str))
        if text is None or rating is None or place is None or user is None:
            raise ValueError("Required attributes not specified!")
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    # ---getter and setter---
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        # check if value is None or value is an empty string
        if not isinstance(value, str):
            raise ValueError("Text must be a string.")
        value = value.strip()
        if len(value) == 0:
            raise ValueError("Text must be a non-empty string.")
        self._text = value
        self.save()

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise ValueError("Rating must be an integer.")
        if value > 5 or value < 1:
            raise ValueError("Rating must be between 1 and 5.")
        self._rating = value
        self.save()

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if value is None:
            raise ValueError("Place is required.")
        if not isinstance(value, Place):
            raise ValueError("Input must be a Place object.")
        self._place = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if value is None:
            raise ValueError("User is required.")
        if not isinstance(value, User):
            raise ValueError("Input must be a User object.")
        self._user = value

    # ---methods----

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
