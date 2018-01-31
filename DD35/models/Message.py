from django.db import models
from django.utils import timezone
from .ChatRoom import ChatRoom
from django.contrib.auth.models import User


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)