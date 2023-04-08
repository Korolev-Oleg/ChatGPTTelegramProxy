import telebot
from db.models import User
from loguru import logger

AUTHENTICATED_USERS = ["hustncn", "sabushka77"]


def is_username_authenticate(username):
    ...


def register_user(user: telebot.types.User):
    try:
        return User.get(User.username == user.username), False
    except User.DoesNotExist:
        new_user = User()
        new_user.username = user.username
        new_user.first_name = user.first_name
        new_user.last_name = user.last_name
        new_user._raw_data_ = user.to_json()
        new_user.has_access = user.username in AUTHENTICATED_USERS
        new_user.save()
        logger.info("User {} registered!".format(user.username))
        return new_user, True
