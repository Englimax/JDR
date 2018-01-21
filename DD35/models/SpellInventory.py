from django.db import models
from .SpellUsage import SpellUsage


class SpellInventory(models.Model):
    name = models.CharField(max_length=50, default='')
    list = models.ManyToManyField(SpellUsage)
