from django.db import models
default_image_src = "no_image.png"


class BaseItem(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=300, default='')
    picture = models.ImageField(upload_to='images', default=default_image_src)
