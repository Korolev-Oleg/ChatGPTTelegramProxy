import telebot
from db.models import User

AUTHENTICATED_USERS = ["@hustnct", "@sabushka77"]


def is_username_authenticate(username):
    return username in AUTHENTICATED_USERS


def register_user(user: telebot.types.User):
    new_user = User()
    new_user.username = user.username
    new_user.first_name = user.first_name
    new_user.last_name = user.last_name
    new_user._raw_data_ = user.to_json()
    new_user.save()
