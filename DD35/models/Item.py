from django.db import models
from django.contrib.auth.models import BaseItem
default_image_src = "no_image.png"


class Item(BaseItem):
    weight = models.FloatField(default=0.5)
