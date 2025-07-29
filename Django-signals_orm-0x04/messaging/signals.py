from django.db.models.signals import post_save
from .models import Message, Notification
from django.dispatch import receiver

@receiver(post_save, sender=Message)
def create_notification(sender, created, instance, **kwargs):
    """signal to automatically create notification when a new message is received"""
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)