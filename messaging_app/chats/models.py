from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """custom `User` class defined off of django default user `AbstractUser`"""
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """define the string representation of the custom `User` model"""
        return self.username


class Conversation(models.Model):
    """
    Class serves as a room where conversations hold.
    Many User(s) (at least 2) can send messages here.
    """
    participants = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """define the string representation of the `Conversation` model"""
        usernames = (", ").join(User.username for User in self.participants.all())
        return f"Conversation bertween {usernames}"


class Message(models.Model):
    """
    Message model that defines the unit of every Conversation
    Each Message belong to only one Conversation
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    body = models.TextField()
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_modified = models.BooleanField(default=False)

    def __str__(self):
        """define the string representation of the `Message` model"""
        return f"{self.sender.username} - {self.body[:15]}"
    