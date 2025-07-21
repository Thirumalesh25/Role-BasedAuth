from django.urls import path
from login import views

urlpatterns = [
    path("", views.home),
    path("login/",views.login, name="login"),
    path("login/user/", views.loginuser, name="loginuser"),
]
