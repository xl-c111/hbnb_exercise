from app.persistence.repository import InMemoryRepository
from app.models.place import Place
from app.models.user import User
from app.models.review import Review
from app.models.amenity import Amenity



class HBnBFacade:
    def __init__(self):
        # when a obj is created, it creates an instance of InMemoryRepository and assigns it to the attribute self.user_repo
        # this user_repo will be used to store and manage user data in memory
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        # self.amenity_repo = InMemoryRepository()

    # define a method that takes user_data as input
    def create_user(self, user_data):
        # create a new user obj
        # **user_data takes all the key-value pairs to keyword arguments, and passes it to the class constructor
        user = User(**user_data)
        # add this new user obj to repo
        self.user_repo.add(user)
        # return the new obj
        return user

    # define a method that takes user_id as input
    def get_user(self, user_id):
        # using user_id to look up the corresponding user obj in the repo and return it
        return self.user_repo.get(user_id)

    # define a method that takes email as input
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    # define a method takes two parameters(user_id: the id of user to update; data: a dict containing updated user info)

    def update_user(self, user_id, data):
        # retrieve user obj with given user id
        user = self.user_repo.get(user_id)
        if not user:
            return None
        # fetch the value for the 'first_name' key from data dict and assign it to the attribute first_name of user obj
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        self.user_repo.update(user.id, data)
        return user

    def create_review(self, review_data):
        user = self.user_repo.get(review_data['user_id'])
        place = self.place_repo.get(review_data['place_id'])
        if user is None or place is None:
            raise ValueError("User or Place not found!")
        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            place=place,
            user=user
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_by_attribute('place_id', place_id)

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        review.text = review_data['text']
        review.rating = review_data['rating']
        self.review_repo.update(review.id, review_data)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        self.review_repo.delete(review_id)
        return True

    def place_exists(self, place_id):
        return self.place_repo.get(place_id) is not None

    # Placeholder method for creating a place
    def create_place(self, data):
        required_fields = ['title', 'description',
                           'price', 'latitude', 'longitude', 'owner_id']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing field: {field}")
        # Convert owner_id to owner object
        owner = self.get_user(data['owner_id'])
        if not owner:
            raise ValueError("Owner not found")
        data['owner'] = owner
        data.pop('owner_id')  # Remove owner_id so Place doesn't get it
        place = Place(**data)
        self.place_repo.add(place)
        return place

    # Placeholder method for fetching all places
    def get_all_places(self):
        return self.place_repo.get_all()

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    # Placeholder method for updating a place

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        # Update the place with the provided data
        for key in ['title', 'description', 'price', 'latitude', 'longitude']:
            if key in place_data:
                setattr(place, key, place_data[key])
        self.place_repo.update(place_id, place)
        return place

    # Placeholder method for deleting a place

    def delete_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        self.place_repo.delete(place_id)
        return place

      # Placeholder method for fetching all amenities

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    # Placeholder methof for creating an amenity
    def create_amenity(self, amenity_data):
        # check if place_id is provided
        place_id = amenity_data.get('place_id')
        if not place_id:
            raise ValueError("Missing field: place_id")


    #  ___Mock : always assume the place exists___
        class MockPlace:
            id = place_id
        place = MockPlace()

        from app.models.amenity import Amenity
        amenity = Amenity(
        name=amenity_data['name'],
        description=amenity_data['description'],
        number=amenity_data['number'],
        place_id=place_id
    )
        self.amenity_repo.add(amenity)
        return amenity

    #  _____end the mock part_____

    """   # check if the place exists
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError(f"Place with ID {place_id} does not exist")

        # check if the user is the owner of the place
        if str(place.owner.id) != user_id:
            raise PermissionError("User is not the owner of the place")

        # create the amenity

        from app.models.amenity import Amenity
        amenity = Amenity(
            name=amenity_data['name'],
            description=amenity_data['description'],
            number=amenity_data['number'],
            place_id=place_id
        )
        self.amenity_repo.add(amenity.id, amenity)
        return amenity """

    # Placeholder method for fetching an amenity by ID
    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    # Placeholder method for updating an amenity

    def update_amenity(self, amenity_id, amenity_data):
        existing_amenity = self.amenity_repo.get(amenity_id)
        if not existing_amenity:
            return None
        for key in ['name', 'description', 'number']:
            if key in amenity_data:
                setattr(existing_amenity, key, amenity_data[key])

        self.amenity_repo.update(amenity_id, existing_amenity)
        return existing_amenity

    # Placeholder method for deleting an amenity
    def delete_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        self.amenity_repo.delete(amenity_id)
        return amenity



"""
1, user = User(**user_data)
   - create a new User obj uding provided data "user_data"
   - **user_data means: take all the key-value pairs in the dict called user_data and pass them as keyword arguments to the function or class
     e.g., user_data = {'name': 'Alice', 'age': 25}
           when you do **user_data ---->>> User(**user_data) == User(name='Alice', age=25)
   - add this new uer obj to the repo

2,  return self.user_repo.get_by_attribute('email', email)
   - self.user_repo: an obj that knows how to loop up users in database
   - get_by_attribute('email', email): find the user where the user's email matches the given value
                                       - first 'email' tells the function to search for the email field
                                       - second email is the value you want to match
   - it returns a user obj whose email matches the input email 

3, self.user_repo.all()
   - .all() will retrieve all user objs from database and return them as a list

4,  user.first_name = data['first_name']
   - data['first_name'] retrieve the value for the 'first_name' key from data dict
   - user.first_name refers to the first_name attribute of user object
 """
