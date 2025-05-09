from django.urls import path
from . import views

urlpatterns = [
    path("create_charge/", views.create_charge, name="create_charge"),
    path("charge_list/", views.charge_list, name="charge_list"),
    path("update_charge/<int:pk>/", views.update_charge, name="update_charge"),
    path("delete_charge/<int:pk>/", views.delete_charge, name="delete_charge"),
]
