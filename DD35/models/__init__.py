from django.db import models
from .model_choices import size
from .Item import Item


class Armor(Item):
    is_master = models.BooleanField(default=False)
    size = models.CharField(choices=size, max_length=30)
    armor_bonus = models.IntegerField(default=1)
    dext_max = models.IntegerField(default=1)
    armor_malus = models.IntegerField(default=1)
    spell_fail = models.FloatField(default=0.1)
    speed = models.IntegerField(default=1)
