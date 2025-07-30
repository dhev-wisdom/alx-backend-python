from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    """Message Model"""
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Messages"
        ordering = ['-timestamp']


class Notification(models.Model):
    """Notification Model"""
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="notifications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Notifications"
        ordering = ['-timestamp']


class MessageHistory(models.Model):
    """MessageHistory Model"""
    message = models.ForeignObject(Message, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    old_content = models.TextField()

    class Meta:
        verbose_name_plural = "Message Histories"
        ordering = ['-timestamp']

