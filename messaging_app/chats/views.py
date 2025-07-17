from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Conversation, Message
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset provides standard CRUD actions for managing User instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    

class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for creating and retrieving conversations.
    Allows listing all conversations and creating a new conversation
    by specifying a list of participant user IDs.
    """
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Create a new conversation between multiple users.
        Expects a list of user IDs in the request body under the key 'participants'.
        Validates that all users exist and sets them as participants in the new conversation.
        Returns the created conversation data.
        """
        participants_id = request.data.get('participants')
        if not participants_id or not isinstance(participants_id, list):
            return Response({"error": "Participants must b a list of user IDs"})
        participants = User.objects.filter(user_id__in=participants_id)
        if participants.count() != len(participants_id):
            return Response({"error": "Some participants were not found"}, status=404)
        
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing messages.
    Allows listing messages and sending a new message to an existing conversation.
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Send a message to an existing conversation.
        Expects 'conversation_id', 'sender_id', and 'message_body' in the request body.
        Validates existence of conversation and sender before creating the message.
        Returns the created message data.
        """
        conversation_id = request.data.get("conversation_id")
        message_body = request.data.get("message_body")
        sender_id = request.data.get("sender_id")

        if not conversation_id or not sender_id:
            return Response({"error": "Both conversation_id and sender_id are needed"}, status=404)
        
        conversation = get_object_or_404(Conversation, conversation_id=conversation_id)
        sender = get_object_or_404(User, user_id=sender_id)

        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=message_body
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
