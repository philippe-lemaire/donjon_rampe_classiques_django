from django.shortcuts import render

from .spells import wizard_spells, cleric_spells

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
