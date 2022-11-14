from django.urls import path

from .views import register, login_request, logout_request

app_name = "simple_auth"

urlpatterns = [
    path("register", register, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
]
