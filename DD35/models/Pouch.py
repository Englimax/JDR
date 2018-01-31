from django.db import models
from .BaseItem import BaseItem


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
