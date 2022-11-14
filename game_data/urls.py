from django.urls import path

from . import views

app_name = "game_data"

urlpatterns = [
    path("/sorts_de_mage", views.view_wizard_spells, name="view_wizard_spells"),
]
