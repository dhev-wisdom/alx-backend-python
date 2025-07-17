from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    """
    Serialize the User model to simple (JSON) form
    that can be read by the frontend
    """
    class Meta:
        model = User
        fields = ['user_id', 'email', 'phone_number']


class MessageSerializer(serializers.ModelSerializer):
    """
    Serialize the Message model to simple (JSON) form
    that can be read by the frontend
    """
    sender = UserSerializer(read_only = True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at', 'edited_at', 'is_modified']


class ConversationSerializer(serializers.ModelSerializer):
    """
    Serialize the Conversation model to simple (JSON) form
    that can be read by the frontend
    """
    messages = MessageSerializer(many = True, read_only = True)
    participants = UserSerializer(many = True, read_only = True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'messages', 'participants', 'created_at']

