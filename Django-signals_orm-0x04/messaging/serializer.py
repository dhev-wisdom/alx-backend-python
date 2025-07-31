from rest_framework import serializers
from .models import Message, Notification, MessageHistory

class MessageSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Message
        fields = ["id", "sender", "receiver", "content", "timestamp", "replies", "edited", "is_read"]

    def get_replies(self, obj):
        return MessageSerializer(obj.replies.all(), many=True).data


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class MessageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageHistory
        fields = "__all__"