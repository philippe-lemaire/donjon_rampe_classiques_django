from django.urls import path

from . import views

app_name = "characters"

urlpatterns = [
    path("creer_personnage", views.create_character, name="create_character"),
    path("mes_personnages", views.my_characters, name="my_characters"),
]
