from django.http import HttpResponse, JsonResponse, Http404
import json

from posts.models import Post, Commentary
from users.models import User

import users.auth as auth


def posts(request):
    all_posts = Post.objects.all()

    response = {"posts": [post.to_dict() for post in all_posts]}

    return JsonResponse(response)


def latest_post(request):
    """
    Возвращает последний пост
    """
    try:
        latest = Post.objects.latest('created_at')
    except:
        return JsonResponse({"latest_post": "not_found"})

    if not latest:
        return Http404()

    response = {"latest_post": latest.to_dict()}

    return JsonResponse(response)


def commentaries_by_post_id(request, post_id):
    """
    Возвращает комментарии к посту
    """
    try:
        post = Post.objects.get(id=post_id)
    except:
        return JsonResponse({"commentaries": "not_found"})

    if not post:
        return Http404()

    commentaries = post.commentary_set.all()

    response = {"commentaries": [commentary.to_dict() for commentary in commentaries]}

    return JsonResponse(response)


def add_commentary(request):
    """
    Добавляет комментарий к посту
    Вернуть комментарий
    """
    token = request.COOKIES.get("token")
    if not token:
        print("no token")
        return HttpResponse("Not authorized", status=401)
    if not auth.is_authorized(token):
        print("not authorized")
        return HttpResponse("Not authorized", status=401)

    data = json.loads(request.body)

    if request.method == 'POST':
        author = User.objects.get(token=token)
        post = Post.objects.get(id=data.get('post_id'))
        value = data.get('value')

        commentary = Commentary()
        commentary.author = author
        commentary.post = post
        commentary.value = value
        commentary.save()

        return JsonResponse({'commentary': commentary.to_dict()})

    return JsonResponse({'message': 'Invalid request method.'})


def create_post(request):
    """
    Создает пост
    """
    token = request.COOKIES.get("token")
    if not token:
        print("no token")
        return HttpResponse("Not authorized", status=401)
    if not auth.is_authorized(token):
        print("not authorized")
        return HttpResponse("Not authorized", status=401)

    if request.method == 'POST':
        author = User.objects.get(token=token)

        photo = request.FILES.get('photo')
        description = request.POST.get('description')
        if photo is None:
            return JsonResponse({'message': 'Photo is required.'})
        if description is None:
            return JsonResponse({'message': 'Description is required.'})

        post = Post()
        post.description = request.POST.get('description')
        post.photo = request.FILES.get('photo')
        post.author = author
        post.save()

        return JsonResponse({'message': 'Post created successfully.'})

    return JsonResponse({'message': 'Invalid request method.'})
