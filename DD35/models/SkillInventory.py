from django.db import models
from .Skill import Skill
from .model_choices import base_skills


class SkillInventory(models.Model):
    skills = models.ManyToManyField(Skill)

    # def __init__(self, *args):
    #     self.
    #     for skill in base_skills:
    #         self.skills.m(Skill(name=skill,value=0))
