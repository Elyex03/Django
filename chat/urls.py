# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),  # Add this line
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
