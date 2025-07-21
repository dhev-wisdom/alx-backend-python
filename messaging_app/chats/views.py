from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, filters, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Conversation, Message
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer
from .permissions import IsOwner, IsParticipantOfConversation

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset provides standard CRUD actions for managing User instances.
    """
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    

class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for creating and retrieving conversations.
    Allows listing all conversations and creating a new conversation
    by specifying a list of participant user IDs.
    """
    permission_classes = [permissions.IsAuthenticated, IsParticipantOfConversation]
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
            return Response({"error": "participants must be a list of user IDs"})
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
    permission_classes = [permissions.IsAuthenticated, IsParticipantOfConversation]
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_backends = [filters.SearchFilter]

    def perform_create(self, serializer):
        conversation = serializer.validated_data.get("conversation")
        if self.request.user not in conversation.participants.all():
            return Response({"detail": "You are not a part of this conversation"},
                            status=status.HTTP_403_FORBIDDEN)
        serializer.save(sender=self.request.user)
        
    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)