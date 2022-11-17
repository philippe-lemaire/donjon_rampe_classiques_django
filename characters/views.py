from random import randint

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .models import Character
from .forms import CharacterCreationForm
from donjon_rampe_classiques_django.settings import LOGIN_URL

from .occupations import occupations
from .equipment import equipment
from game_data.utils import threedsix, ability_modifiers
from .birthsigns import birthsigns
from .class_bonuses import (
    level_bonuses,
    mighty_deeds,
    halflin_skills,
    thieves_bonuses,
    thieves_skills,
    luck_die,
)
from .random_names import random_names
from .titles import titles
from .equipment import equipment
from game_data.spells import wizard_spells, cleric_spells


@login_required
def create_character(request):
    """Super dummy view, still todo"""
    if request.method == "POST":
        form = CharacterCreationForm(request.POST)
        if form.is_valid():
            # création du personnage proprement dit
            character = Character()
            character.name = form.cleaned_data["name"] or "Anonyme"
            character.user = request.user
            character.nickname = ""  # TODO add randomtables for nicknames
            character.level = 0
            character.classe = "Paysan"
            character.xp = 0
            character.title = ""  # TODO add randomtables for titles
            occupation_roll = randint(1, 100)
            character.occupation = occupations[occupation_roll][0]
            character.proficient_weapons = occupations[occupation_roll][1]
            character.inventory = f"{occupations[occupation_roll][1]}, {occupations[occupation_roll][2]}, {equipment.get(randint(1,24))[0]}"

            character.strength = threedsix()
            character.agility = threedsix()
            character.stamina = threedsix()
            character.personality = threedsix()
            character.intelligence = threedsix()
            character.luck = threedsix()
            # derived stats
            character.hp = randint(1, 4) + ability_modifiers[character.stamina]
            if character.hp < 1:
                character.hp = 1

            character.current_hp = character.hp
            character.reflex = ability_modifiers[character.agility]
            character.fortitude = ability_modifiers[character.stamina]
            character.will = ability_modifiers[character.personality]
            character.ac = 10 + ability_modifiers[character.agility]

            character.speed = 9
            if "Nain" in character.occupation or "Halfelin" in character.occupation:
                character.speed = 6

            character.init = ability_modifiers[character.agility]
            birth_sign_roll = randint(1, 30)
            character.birthsign = birthsigns[birth_sign_roll][0]
            luck_mod = ability_modifiers[character.luck]
            if luck_mod >= 0:
                character.birthsign_effect = (
                    f"{birthsigns[birth_sign_roll][1]} (+{luck_mod})"
                )
            else:
                character.birthsign_effect = (
                    f"{birthsigns[birth_sign_roll][1]} ({luck_mod})"
                )

            character.languages = "Commun"

            character.patron = ""
            character.deity = ""
            character.spells_known = str([])
            character.dead = False

            # save the char
            character.save()

            # redirect to my characters or character detail
            # add a success message before
            messages.success(request, "Personnage créé.")
            return HttpResponseRedirect(reverse("characters:my_characters"))
    else:
        # build context with empty form
        context = {"form": CharacterCreationForm()}

    return render(request, "characters/create_character.html", context)


class my_characters(LoginRequiredMixin, ListView):
    model = Character
    paginate_by = 10  # if pagination is desired
    template_name = "characters/my_characters.html"
    context_object_name = "characters"

    # redirect_field_name = "personnages/mes_personnages"

    def get_queryset(self):
        return Character.objects.filter(user=self.request.user)


class character_detail(LoginRequiredMixin, DetailView):
    model = Character
    template_name = "characters/character_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mod"] = ability_modifiers
        context["level_bonuses"] = level_bonuses
        context["mighty_deeds"] = mighty_deeds
        context["titles"] = titles
        context["halflin_skills"] = halflin_skills
        context["thieves_bonuses"] = thieves_bonuses
        context["thieves_skills"] = thieves_skills
        context["luck_die"] = luck_die

        return context
