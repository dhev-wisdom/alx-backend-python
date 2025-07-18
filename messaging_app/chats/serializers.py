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
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at', 'edited_at', 'is_modified']
        read_only_fields = ['is_modified']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')

        if request and request.method in ['PUT', 'PATCH']:
            fields['sender'].read_only = True
            fields['conversation'].read_only = True

        return fields

    def validate_message_body(self, value):
        if (len(value.strip()) == 0):
            raise serializers.ValidationError("Message cannot be empty")
        return value
    
    def update(self, instance, validated_data):
        original_body = instance.message_body
        new_body = validated_data.get("message_body", original_body)

        if original_body != new_body:
            instance.is_modified = True

        return super().update(instance, validated_data)


class ConversationSerializer(serializers.ModelSerializer):
    """
    Serialize the Conversation model to simple (JSON) form
    that can be read by the frontend
    """
    messages = MessageSerializer(many = True)
    participants = UserSerializer(many = True)
    message_count = serializers.SerializerMethodField()

    def get_message_count(self, obj):
        return obj.messages.count()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'messages', 'participants', 'created_at', 'message_count']

