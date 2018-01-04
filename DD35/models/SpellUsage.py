from django.db import models
from django.contrib.auth.models import Spell
default_image_src = "no_image.png"


class SpellUsage(models.Model):
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    spell_per_day = models.IntegerField(default=1)
    spell_remaining = models.IntegerField(default=1)
