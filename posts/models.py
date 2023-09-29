from django.db import models


class User(models.Model):
    email = models.EmailField("Email")
    name = models.CharField("Имя пользователя", max_length=30)
    avatar = models.ImageField("Аватар", upload_to="avatars")


class Post(models.Model):
    photo = models.ImageField("Фото", upload_to="post_photos")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Название фото", max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField(null=True, default=None)
    description = models.CharField("Описание", max_length=5000)


class Mark(models.Model):
    class Vote(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(choices = Vote.choices)


class Commentary(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField("Комментарий", max_length=5000)
