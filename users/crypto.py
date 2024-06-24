import uuid


def create_token():
    """
    Создает токен
    """
    return uuid.uuid4().hex

