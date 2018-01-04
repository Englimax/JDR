from django.db import models
from django.contrib.auth.models import User
from .model_choices import *
default_image_src = "no_image.png"


class Player(User):
    pass























class BaseItem(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=300, default='')
    picture = models.ImageField(upload_to='images', default=default_image_src)


class Item(BaseItem):
    weight = models.FloatField(default=0.5)


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


class ItemInventory(models.Model):
    location = models.CharField(default="Sur soi", max_length=50)
#    charac = models.ForeignKey(PlayedCharacter, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name="Items")
    bourse = models.ForeignKey(Pouch, on_delete=models.CASCADE, related_name="Pouch")


class Weapon(Item):
    is_master = models.BooleanField(default=False)
    size = models.CharField(choices=size, max_length=30)
    wp_type = models.CharField(max_length=30)  # contondant, tranchant, perforant...
    damage = models.CharField(max_length=10)
    critical = models.CharField(max_length=10)
    wp_range = models.IntegerField(default=1)


class Armor(Item):
    is_master = models.BooleanField(default=False)
    size = models.CharField(choices=size, max_length=30)
    armor_bonus = models.IntegerField(default=1)
    dext_max = models.IntegerField(default=1)
    armor_malus = models.IntegerField(default=1)
    spell_fail = models.FloatField(default=0.1)
    speed = models.IntegerField(default=1)
    

class PlayedCharacter(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    race = models.IntegerField(choices=races)
    classes = models.IntegerField(choices=classes)
    order = models.IntegerField(choices=order)
    manich = models.IntegerField(choices=alignment)
    god = models.CharField(max_length=30)
    
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    size = models.CharField(choices=size, max_length=30)
    age = models.IntegerField(default=18)
    gender = models.CharField(choices=(("1", "Homme"), ("2", "Femme")), max_length=30)
    
    height = models.IntegerField(default=100)
    weight = models.IntegerField(default=75)
    eyes = models.CharField(max_length=50)
    hair = models.CharField(max_length=50)
    
    attributes = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    skills = models.ForeignKey(SkillInventory, on_delete=models.CASCADE)
    inventory = models.ForeignKey(ItemInventory, on_delete=models.CASCADE)
    various_mod = models.ForeignKey(VariousModificator, on_delete=models.CASCADE)
    spells = models.ForeignKey(SpellInventory, on_delete=models.CASCADE)
