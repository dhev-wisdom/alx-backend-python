from django.contrib import admin
from .models import Message,  Notification

# Register your models here.
admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','sender', 'receiver', 'content', 'timestamp', 'is_modified', 'is_read')
    list_filter = ('sender', 'receiver', 'timestamp', 'is_modified', 'is_read')


admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'content', 'timestamp', 'is_read')
    list_filter = ('user', 'is_read', 'timestamp')
