from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("update_user/", views.update_user_profile, name="update_user")
]
