from django.db import models
from users.models import User


class Post(models.Model):
    photo = models.ImageField("Фото", upload_to="post_photos")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Название фото", max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField(null=True, default=None)
    description = models.CharField("Описание", max_length=5000, null=True)

    def to_dict(self):
        return {
            "id": self.id,
            "photo": self.photo.url,
            "author": self.author.id,
            "name": self.name,
            "created_at": str(self.created_at),
            "posted_at": str(self.posted_at),
            "description": self.description,
        }


class Mark(models.Model):
    class Vote(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(choices=Vote.choices)

    def to_dict(self):
        return {
            "id": self.id,
            "post": self.post.id,
            "author": self.author.id,
            "value": self.value,
        }


class Commentary(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField("Комментарий", max_length=5000)

    def to_dict(self):
        return {
            "id": self.id,
            "post": self.post.id,
            "author": self.author.id,
            "value": self.value,
        }
