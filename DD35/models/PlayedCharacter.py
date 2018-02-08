from django.db import models
from .Attribute import Attribute
from .SkillInventory import SkillInventory
from .ItemInventory import ItemInventory
from .VariousModificator import VariousModificator
from .SpellInventory import SpellInventory
from .Campaign import Campaign
from .Player import Player
from .model_choices import order
from .model_choices import classes
from .model_choices import races
from .model_choices import alignment
from .model_choices import size


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
    attributes = models.OneToOneField(Attribute, on_delete=models.CASCADE, related_name='player')
    skills = models.OneToOneField(SkillInventory, on_delete=models.CASCADE, related_name='player')
    inventory = models.OneToOneField(ItemInventory, on_delete=models.CASCADE, related_name='player')
    various_mod = models.OneToOneField(VariousModificator, on_delete=models.CASCADE, related_name='player')
    spells = models.OneToOneField(SpellInventory, on_delete=models.CASCADE, related_name='player')

    def jsonified(self):
        return {
        "name": self.name,
        "surname": self.surname,
        "alias": self.alias,
        "campaign": self.campaign,
        "player": self.player,
        "race": self.race,
        "classes": self.classes,
        "order": self.order,
        "manich": self.manich,
        "god": self.god,
        "level": self.level,
        "xp": self.xp,
        "size": self.size,
        "age": self.age,
        "gender": self.gender,
        "height": self.height,
        "weight": self.weight,
        "eyes": self.eyes,
        "hair": self.hair,
        "attributes": self.attributes,
        "skills": self.skills,
        "inventory": self.inventory,
        "various_mod": self.various_mod,
        "spells": self.spells,
    }
