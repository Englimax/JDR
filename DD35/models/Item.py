from django.db import models
from .BaseItem import BaseItem


class Item(BaseItem):
    weight = models.FloatField(default=0.5)
