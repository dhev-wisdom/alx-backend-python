from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    """Message Model"""
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_modified = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)


class Notification(models.Model):
    """Notification Model"""
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="notifications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    is_read = models.BooleanField(default=False)

