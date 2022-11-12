from django.db import models
from django.conf import settings


# Create your models here.


class Character(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.TextField(max_length=200)
    nickname = models.TextField(max_length=200, null=True, blank=True)
    level = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    classe = models.TextField(max_length=200)
    xp = models.IntegerField()
    title = models.TextField(max_length=200, null=True, blank=True)
    occupation = models.TextField(max_length=200, null=True, blank=True)
    ac = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    hp = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    current_hp = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    speed = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    init = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    strength = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    agility = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    stamina = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    personality = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    intelligence = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    luck = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    reflex = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    fortitude = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    will = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    alignment = models.TextField(max_length=200)
    birthsign = models.TextField(max_length=200)
    birthsign_effect = models.TextField(max_length=200)
    languages = models.TextField(max_length=200, null=True, blank=True)
    patron = models.TextField(max_length=200, null=True, blank=True)
    spells_known = models.TextField(max_length=200, null=True, blank=True)
    inventory = models.TextField(max_length=200, null=True, blank=True)
    proficient_weapons = models.TextField(max_length=200, null=True, blank=True)
    lucky_weapon = models.TextField(max_length=200, null=True, blank=True)
    lucky_spell = models.TextField(max_length=200, null=True, blank=True)
    dead = models.BooleanField()
    curses = models.TextField(max_length=200, null=True, blank=True)
    deity = models.TextField(max_length=200, null=True, blank=True)
