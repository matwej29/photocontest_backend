import datetime
import json

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
import users.auth as auth


def login(request):
    # TODO: verify email
    data = json.loads(request.body)
    email = data.get('email')

    registration_token = auth.login(email)
    # send by email instead of JsonResponse
    return JsonResponse({"registration_token": registration_token})


# TODO: придумать нормальное название
def verify_login(request):
    data = json.loads(request.body)
    registration_token = data.get('registration_token')

    try:
        user = auth.create_token(registration_token)
    except:
        # тут надо сказать, что регистрационный токен некорректен
        return HttpResponseNotFound()

    response = HttpResponse()

    response.set_cookie("token", value=user.token,
                        httponly=True,
                        max_age=datetime.timedelta(days=10))
    # TODO: samesite?
    # TODO: secure?

    response.status_code = 200

    return response


def is_authorized(request):
    token = request.COOKIES.get('token')

    if not token:
        return HttpResponse("Not authorized", status=401)
    # http 401 is not the best choice
    # because it is used for authentication
    # but we are not authenticated yet

    is_authorized = auth.is_authorized(token)
    if not is_authorized:
        return HttpResponse("Not authorized", status=401)

    return HttpResponse(status=200)


def clear_cookie(request):
    response = HttpResponse()
    response.delete_cookie("token")
    return response
