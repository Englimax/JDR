from django.db import models
from .model_choices import *
default_image_src = "no_image.png"


class Attribute(models.Model):
    force = models.IntegerField(default=10)
    dex = models.IntegerField(default=10)
    con = models.IntegerField(default=10)
    intell = models.IntegerField(default=10)
    sag = models.IntegerField(default=10)
    cha = models.IntegerField(default=10)
    pv = models.IntegerField(default=9)
    pv_temp = models.IntegerField(default=0)
    dmg_reduction = models.IntegerField(default=0)
    ca = models.IntegerField(default=10)
    deplacement = models.IntegerField(default=9)
    initiative = models.IntegerField(default=0)
    base_atk_bonus = models.IntegerField(default=0)
    reflexes = models.IntegerField(default=0)
    vigueur = models.IntegerField(default=0)
    volonte = models.IntegerField(default=0)
    poids_transp = models.FloatField(default=17.5)