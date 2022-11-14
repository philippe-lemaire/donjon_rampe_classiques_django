from django import forms


class CharacterCreationForm(forms.Form):
    name = forms.CharField(
        label="Nom du personnage, laisser vide pour un nom aléatoire, qui sera attribué au niveau 1.",
        max_length=100,
        required=False,
    )
