from .models import User
import users.crypto as crypto
from django.utils import timezone
import datetime


class UserNotFound(Exception):
    pass


def create_registration_token(user) -> str:
    """
    Создает пользователя
    """
    registration_token = crypto.create_token()
    expiration_date = timezone.now() + datetime.timedelta(minutes=10)

    user.registration_token = registration_token
    user.expiration_date = expiration_date

    user.save()

    return registration_token


def create_token(registration_token) -> User:
    if user := User.objects.get(registration_token=registration_token):
        user.token = crypto.create_token()
        user.expiration_date = timezone.now() + datetime.timedelta(days=10)

        user.save()
        return user
    else:
        raise UserNotFound("Не найдем пользователь с таким registration_token. Надо нормальное исключение сделать")


def login(email):
    user = User.objects.get_or_create(email=email)[0]

    registration_token = create_registration_token(user)

    return registration_token


def is_authorized(token):
    try:
        user = User.objects.get(token=token)
    except:
        return False

    if user.expiration_date < timezone.now():
        return False

    return True
