from django.db.models.signals import post_save, pre_save
from .models import Message, Notification, MessageHistory
from django.dispatch import receiver

@receiver(post_save, sender=Message)
def create_notification(sender, created, instance, **kwargs):
    """signal to automatically create notification when a new message is received"""
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance,
            content=instance.content
        )

@receiver(pre_save, sender=Message)
def update_message_logs(sender, instance, **kwargs):
    """signal to update keep track of edited messages and message history"""
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                instance.edited = True
                MessageHistory.objects.create(
                    message=old_message,
                    old_content=old_message.content,
                    edited_by=getattr(instance, '_edited_by', old_message.sender)
                )
                Notification.objects.create(
                    user=instance.receiver,
                    message=instance,
                    content=instance.content
                )
        except Message.DoesNotExist:
            pass