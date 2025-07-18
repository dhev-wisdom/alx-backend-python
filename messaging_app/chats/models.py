from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
import uuid

class User(AbstractUser):
    """custom `User` class defined off of django default user `AbstractUser`"""
    user_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    # password = models.CharField(max_length=128, verbose_name="Password (Hashed)")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # def save(self, *args, **kwargs):
    #     self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

    def __str__(self):
        """define the string representation of the custom `User` model"""
        return self.username


class Conversation(models.Model):
    """
    Class serves as a room where conversations hold.
    Many User(s) (at least 2) can send messages here.
    """
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    message_body = models.TextField()
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sent_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    is_modified = models.BooleanField(default=False)

    def __str__(self):
        """define the string representation of the `Message` model"""
        return f"{self.sender.username} - {self.message_body[:15]}"
    