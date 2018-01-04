from django.db import models
default_image_src = "no_image.png"


class VariousModificator(models.Model):
    modificator_name = models.CharField(max_length=150)
    modificator_description = models.CharField(max_length=500)
