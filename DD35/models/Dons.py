from django.db import models
from .model_choices import *
default_image_src = "no_image.png"


class Dons(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='')
