from django.shortcuts import render
from django.contrib import messages

from .spells import wizard_spells, cleric_spells
from .fumbles import fumbles
from utils.roll import roll

# Create your views here.


def view_wizard_spells(request):
    context = {"spells": wizard_spells}

    return render(
        request, template_name="game_data/view_wizard_spells.html", context=context
    )


def view_cleric_spells(request):
    context = {"spells": cleric_spells}

    return render(
        request, template_name="game_data/view_cleric_spells.html", context=context
    )


def view_fumbles(request):
    context = {"fumbles": fumbles}
    return render(request, "game_data/fumbles.html", context)


def roll_fumbles(request, die_size):
    result = roll(die_size)
    messages.success(
        request,
        f"Votre résultat naturel : {result}. Ajustez-le en soustrayant votre bonus de chance.",
    )
    return view_fumbles(request)
