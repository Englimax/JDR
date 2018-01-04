from django.db import models
from django.contrib.auth.models import User
from .model_choices import *
default_image_src = "no_image.png"


class Player(User):
    pass
