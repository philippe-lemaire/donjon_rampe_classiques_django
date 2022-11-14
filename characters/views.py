from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Character


@login_required
def create_character(request):
    """Super dummy view, still todo"""
    return render(request, "characters/create_character.html")


@login_required
def my_characters(request):
    """dummy view for now. Move to a generic view with additional filter on characters I own?"""
    return render(request, "characters/my_characters.html", context={"characters": []})
