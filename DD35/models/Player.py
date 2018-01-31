from django.contrib.auth.models import User
from django.db import models


class Player(User):
    short_name = models.CharField(max_length=30)
