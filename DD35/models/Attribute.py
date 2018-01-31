from django.db import models


class Attribute(models.Model):
    force = models.IntegerField(default=10)
    dex = models.IntegerField(default=10)
    con = models.IntegerField(default=10)
    intell = models.IntegerField(default=10)
    sag = models.IntegerField(default=10)
    cha = models.IntegerField(default=10)
    pv = models.IntegerField(default=9)
    pv_temp = models.IntegerField(default=0)
    dmg_reduction = models.IntegerField(default=0)
    ca = models.IntegerField(default=10)
    deplacement = models.IntegerField(default=9)
    initiative = models.IntegerField(default=0)
    base_atk_bonus = models.IntegerField(default=0)
    reflexes = models.IntegerField(default=0)
    vigueur = models.IntegerField(default=0)
    volonte = models.IntegerField(default=0)
    poids_transp = models.FloatField(default=17.5)

    def jsonified(self):
        return {
            "Force": self.force,
            "Dextérité": self.dex,
            "Constitution": self.con,
            "Intelligence": self.intell,
            "Sagesse": self.sag,
            "Charisme": self.cha,
            "PV": self.pv,
            "PV temporaire": self.pv_temp,
            "Réduction des dégâts": self.dmg_reduction,
            "CA": self.ca,
            "Déplacement": self.deplacement,
            "Initiative": self.initiative,
            "Bonus de base à l'attaque": self.base_atk_bonus,
            "Réflexes": self.reflexes,
            "Vigueur": self.vigueur,
            "Volonté": self.volonte,
            "Poids transportable": self.poids_transp,
        }
