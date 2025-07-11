# DataAccessLayer
class DataAccessLayer():
    # Stores user data as key-value pairs: user_id -> user_name
    def __init__(self):
        # initialize an empty dict called data to hold key=value pairs(user_id: user_name)
        self.data = {}

    def get(self, key):
        # retrieve the value associstaed with the given key
        return self.data.get(key)

    def set(self, key, value):
        # add a new entry or update the exsting entry to the dict for the given key
        self.data[key] = value


# Business Logic Layer
class BusinessLogicLayer:
    # constructor: takes the dal instance as an argument to init
    def __init__(self, dataaccesslayer):
        # store the data access layer instance as an attribute
        self.dataaccesslayer = dataaccesslayer

    def add_user(self, user_id, user_name):
        # check if user_id and user_name is missing or invalid(None or empty string"")
        if not user_id or not user_name:
            raise ValueError("Invalid user data")
        # set method using user_id as key to store user_name
        self.dataaccesslayer.set(user_id, user_name)

    def get_user(self, user_id):
        # get method using user_id as key to retrieve user_name
        return self.dataaccesslayer.get(user_id)


# Presentation Layer(This layer handles interactions with users(print output))
class PresentationLayer:
    # takes bll instance as argument
    def __init__(self, businesslogiclayer):
        self.businesslogiclayer = businesslogiclayer

    # define a method usingz user_id as input
    def display_user(self, user_id):
        # call the get method from bll to retrieve user_name using user_id as the key
        user = self.businesslogiclayer.get_user(user_id)
        # check if user is found(not None or empty)
        if user:
            print("User ID: {}, User Name: {}".format(user_id, user))
        else:
            print("User not found!")

    # define a method to add new user through th interface
    def add_user_interface(self, user_id, user_name):
        try:
            # Call add_user from the business logic layer with user_id and user_name
            self.businesslogiclayer.add_user(user_id, user_name)
            print("User added successfully")
        except ValueError as e:
            print(e)
