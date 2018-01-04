from django.db import models
from DD35.models import SpellUsage
from .model_choices import *
default_image_src = "no_image.png"


class SpellInventory(models.Model):
    name = models.CharField(max_length=50, default='')
    list = models.ManyToManyField(SpellUsage)
