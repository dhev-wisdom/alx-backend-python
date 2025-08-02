from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UnreadMessagesManager(models.Manager):
    """Custom manager to filter unread messages for a user"""
    def for_user(self, user):
        return self.get_queryset().filter(receiver=user, edited=False).only(
            "id", "sender", "receiver", "content", "timestamp"
        )