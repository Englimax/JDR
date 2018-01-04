from django.db import models
from django.contrib.auth.models import Item
from .model_choices import size
default_image_src = "no_image.png"


class Weapon(Item):
    is_master = models.BooleanField(default=False)
    size = models.CharField(choices=size, max_length=30)
    wp_type = models.CharField(max_length=30)  # contondant, tranchant, perforant...
    damage = models.CharField(max_length=10)
    critical = models.CharField(max_length=10)
    wp_range = models.IntegerField(default=1)
