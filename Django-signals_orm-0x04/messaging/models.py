from django.db import models
from django.contrib.auth import get_user_model
from .managers import UnreadMessagesManager

User = get_user_model()


class Message(models.Model):
    """Message Model"""
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    parent_message = models.ForeignKey("self", blank=True, null=True, related_name="replies", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    objects = models.Manager()
    unread = UnreadMessagesManager()

    class Meta:
        verbose_name_plural = "Messages"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.content[:15]} - from {self.sender.username} to {self.receiver.username}"


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

    def __str__(self):
        return f"Notification for {self.user.username}: {self.content[:15]}"


class MessageHistory(models.Model):
    """MessageHistory Model"""
    message = models.ForeignKey(Message, related_name="history", on_delete=models.CASCADE)
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(User, related_name="edits", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Message Histories"
        ordering = ['-edited_at']

    def __str__(self):
        return f"{self.message.content[:15]} - edited by {self.edited_by} at {self.edited_at}"

