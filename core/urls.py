from django.urls import path
from . import views

urlpatterns = [
    path("create_charge/", views.create_charge, name="create_charge"),
    path("charge_list/", views.charge_list, name="charge_list"),
]
