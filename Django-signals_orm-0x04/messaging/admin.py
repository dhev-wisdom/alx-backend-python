from django.contrib import admin
from .models import Message,  Notification, MessageHistory

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','sender', 'receiver', 'content', 'timestamp', 'edited', 'is_read')
    list_filter = ('sender', 'receiver', 'timestamp', 'edited', 'is_read')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'content', 'timestamp', 'is_read')
    list_filter = ('user', 'is_read', 'timestamp')


@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'old_content', 'edited_at')
    list_filter = ('edited_at', 'edited_at')
