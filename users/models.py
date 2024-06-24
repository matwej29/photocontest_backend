from django.db import models


class User(models.Model):
    email = models.EmailField("Email")
    name = models.CharField("Имя пользователя", max_length=30)
    avatar = models.ImageField("Аватар", default=None, null=True, upload_to="avatars")

    token = models.CharField("Токен", max_length=100, null=True)
    expiration_date = models.DateTimeField("Дата истечения токена", null=True)

    registration_token = models.CharField("Регистрационный токен", max_length=50, null=True)
    registration_token_expiration_date = models.DateTimeField("Дата истечения токена регистрации", null=True)

    def __str__(self):
        return self.email

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "avatar": self.avatar.url if self.avatar else None,
        }

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["name"]
