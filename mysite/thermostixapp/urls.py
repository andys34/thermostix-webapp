from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index),
    path("pushdata", views.PushData),
    path("admin", views.AdminView),
    path("addUser", views.AddUser),
    path("addThermometer", views.AddThermometer),
    path("assignThermometersToUser", views.AssignThermometersToUser),
]
