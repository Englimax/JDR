from django.db import models
from django.contrib.auth.models import BaseItem
default_image_src = "no_image.png"


class Pouch(BaseItem):
    po = models.IntegerField(default=0)
    pa = models.IntegerField(default=0)
    pc = models.IntegerField(default=0)
    pp = models.IntegerField(default=0)

    @property
    def weight(self):
        return (
            getattr(self, self.po.attname)/100. +
            getattr(self, self.po.attname)/100. +
            getattr(self, self.po.attname)/100. +
            getattr(self, self.po.attname)/100.
        )
