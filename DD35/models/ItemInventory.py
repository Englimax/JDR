from django.db import models
from django.contrib.auth.models import Pouch
from django.contrib.auth.models import Item
default_image_src = "no_image.png"


class ItemInventory(models.Model):
    location = models.CharField(default="Sur soi", max_length=50)
#    charac = models.ForeignKey(PlayedCharacter, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name="Items")
    bourse = models.ForeignKey(Pouch, on_delete=models.CASCADE, related_name="Pouch")
