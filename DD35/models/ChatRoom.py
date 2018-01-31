from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=200)
    list_of_users = models.ManyToManyField(User, related_name="chatrooms")  # TODO : changer nom

    def is_present(self, user):
        return (user in self.list_of_users)

