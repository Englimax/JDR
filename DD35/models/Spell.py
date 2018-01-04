from django.db import models
default_image_src = "no_image.png"

class Spell(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='')
    level = models.IntegerField(default=0)
    per_day = models.IntegerField(default=1)
    remaining = models.IntegerField(default=1)
    dd_sauv = models.IntegerField(default=10)
