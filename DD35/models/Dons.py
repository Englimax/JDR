from django.db import models


class Dons(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='')


