import uuid
from datetime import datetime
import re
import hashlib
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class User:
    # a list of User objects
    users_db = []

    def __init__(self, first_name, last_name, email, is_admin, password):
        if first_name is None or last_name is None or email is None or is_admin is None or password is None:
            raise ValueError("Required attributes not specified!")
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password
        self.reviews = []
        self.places = []
        self.amenities = []

    # ---getter and setter---
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("First name must be a string.")
        value = value.strip()
        if len(value) == 0:
            raise ValueError("First name cannot be empty.")
        if not 1 <= len(value) <= 50:
            raise ValueError(
                "First name length must be between 1 and 50 characters.")
        if not value.replace(" ", "").isalpha():
            raise ValueError("First name can only contain letters and spaces.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string.")
        value = value.strip()
        if len(value) == 0:
            raise ValueError("Last name cannot be empty.")
        if not 1 <= len(value) <= 50:
            raise ValueError(
                "Last name length must be between 1 and 50 characters.")
        if not value.replace(" ", "").isalpha():
            raise ValueError("Last name can only contain letters and spaces.")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        value = value.strip().lower()
        if not re.fullmatch(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$", value):
            raise ValueError("Invalid email format.")
        self._email = value

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        if not isinstance(value, bool):
            raise ValueError(
                "is_admin must be a boolean value (True or False).")
        self._is_admin = value

    # for security reason, others should not be allowed to access the password
    @property
    def password(self):
        raise AttributeError("Password is write-only for security reasons.")
    # only setter method should be kept

    @password.setter
    def password(self, value):
        if not value or len(value) < 8:
            raise ValueError("Password must be at least 8 characters.")
        self._password = hashlib.sha256(value.encode()).hexdigest()

    # ---methods---

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def register(self):
        # loop through the User-Obj list to check if user's email matches new user's email
        for user in User.users_db:
            if user.email == self.email:
                raise ValueError("Email already registered.")
        User.users_db.append(self)
        print(f"User {self.email} registered successfully.")

    def update_profile(self, first_name=None, last_name=None, email=None, password=None):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        self.save()

    def delete_account(self):
        if self in User.users_db:
            User.users_db.remove(self)
            print(f"User {self.email} deleted.")
        else:
            print("User not found.")

    def write_review(self, review):
        if self.is_admin:
            raise PermissionError(
                "Owner/admin is not allowed to write reviews.")
        if not isinstance(review, Review):
            raise ValueError("Input must be a Review object.")
        self.reviews.append(review)

    def add_place(self, place):
        # check the parameter place is an instance of Place class
        if not self.is_admin:
            raise PermissionError("Only owner/admin can add places.")
        if not isinstance(place, Place):
            raise ValueError("Input must be a Place object.")
        place.owner = self
        self.places.append(place)


"""
1, Syntax: value.replace(" ", "").isalpha(): 
   - .replace(" ", "") removes all the spaces from the string
   - .isalpha() is str method that checks if the string only has letters

2, Syntax: re.fullmatch(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", value)
   - re.fullmatch() is a function means that entire value string must match the regex(not just a part)
   - r"..." refers to the raw string
   - ^: the start of string 
   - [A-Za-z0-9._%+-]+: matches the username part of the email; allows one or more (+) of uppercase letters,
     lowercase letters, digits, dot (.), underscore (_), percent (%), plus (+), and minus (-)
   - @: must have a @ symbol
   - [A-Za-z0-9.-]+: matches the domain part of the email; allows one or more letters, digits, dot (.), and minus (-)
   - \.: must have a dot 
   - [A-Za-z]{2,}: matches the email suffix(com, cn, org); must have at least 2 letters  

3, Syntax: hashlib.sha256(value.encode()).hexdigest()
   - value.encode(): converts textplain string into bytes
   - hashlib is a standard Python library for hashing
   - sha256 is a widely used secure hash algorithm
   - hashlib.sha256(value.encode()) returns a SHA-256 hash object
   - .hexdigest() turns a hash obj into a hexadecimal string

4, Syntax: .strip(): remove leading and trailing spaces

5, Syntax: .strip().lower(): remove leading and trailing spaces and convert email to lowercase 
 
6, - User login and registeration with email(which is unique, but can be changed);
   - Inside your database and system, use uuid as unique and unchangale ID to find users, places;
   - To check if someone is owner, compare the user's uuid with place owner's uuid or compare user obj directly
        if user.if == place.owner.id  or if user == place.owner
   - To check if a user is an admin, look at thier is_admin field 
        if self.is_admin

"""
