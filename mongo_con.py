import pymongo
from mongoengine import *
import os

# con = pymongo.MongoClient("mongodb+srv://adam:Test123@cluster0-lyp3x.mongodb.net/test?retryWrites=true&w=majority")
connect(host="mongodb+srv://adam:Test123@cluster0-lyp3x.mongodb.net/chats?retryWrites=true&w=majority")


class User(Document):
    username = StringField(unique=True, required=True)
    email = EmailField(unique=False)
    password = StringField(required=True)

    meta = {
        "indexes": ["username"]
    }

    def json(self):
        user_dict = {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
        return user_dict


def create_user(username, email, password):
    try:
        u = User(username=username,
                 email=email, password=password)
        u.save()
        return u
    except NotUniqueError:
        print("Not unique username")


def check_user(username, password):
    selected_user = None
    try:
        selected_user = User.objects(username=username, password=password).get()
        return selected_user.username
    except DoesNotExist:
        print("Username, and password", username, password, "not found")



# FILTERING
# admin = User.objects()


# for a in admin:
# print(a.username)

# Get single unique result
# john_doe = User.objects(username="ben").get()
