from django.db import models
default_image_src = "no_image.png"


class Campaign(models.Model):
    name = models.CharField(max_length=50)
#    md = models.ManyToManyField(Player, related_name = "DM")
#    players = models.ManyToManyField(Player, related_name = "Player")
    version = models.IntegerField(default=1)
