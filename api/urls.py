from django.urls import path

from . import views
import users.views

urlpatterns = [
    path("posts", views.posts),
    path("posts/latest", views.latest_post),
    path("commentaries/<int:post_id>", views.commentaries_by_post_id),
    path("add_commentary", views.add_commentary),
    path("login", users.views.login),
    path("verify_login", users.views.verify_login, name="verify_login"),
    path("is_authorized", users.views.is_authorized, name="is_authorized"),
    path("create_post", views.create_post, name="create_post"),
    path("clear_cookie", users.views.clear_cookie, name="clear_cookie"),
]
