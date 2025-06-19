from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.review import Review


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
