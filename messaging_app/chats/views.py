from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, filters, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied, ValidationError
from .models import User, Conversation, Message
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer
from .permissions import IsOwner, IsParticipantOfConversation
from .pagination import MessageResultSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MessageFilter

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset provides standard CRUD actions for managing User instances.
    """
    permission_classes = [permissions.IsAuthenticated]
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
            raise ValidationError("participants must be a list of user IDs")
        participants = User.objects.filter(user_id__in=participants_id)
        if participants.count() != len(participants_id):
            raise ValidationError("Some participants were not found")
        
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        """Handles full updates (PUT)"""
        instance = self.get_object()
        participants_id = request.data.get('participants')
        if not participants_id or not isinstance(participants_id, list):
            raise ValidationError("participants must be a list of user IDs")

        participants = User.objects.filter(user_id__in=participants_id)
        if participants.count() != len(participants_id):
            raise ValidationError("Some participants were not found")

        instance.participants.set(participants)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        """Handles partial updates (PATCH)"""
        instance = self.get_object()
        participants_id = request.data.get('participants')
        if participants_id:
            if not isinstance(participants_id, list):
                raise ValidationError("participants must be a list of user IDs")

            participants = User.objects.filter(user_id__in=participants_id)
            if participants.count() != len(participants_id):
                raise ValidationError("Some participants were not found")

            instance.participants.set(participants)

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing messages.
    Allows listing messages and sending a new message to an existing conversation.
    """
    permission_classes = [permissions.IsAuthenticated, IsParticipantOfConversation]
    serializer_class = MessageSerializer
    pagination_class = MessageResultSetPagination
    queryset = Message.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

    def perform_create(self, serializer):
        conversation = serializer.validated_data.get("conversation")
        if self.request.user not in conversation.participants.all():
            raise PermissionDenied("You are not a part of this conversation")
            # return Response({"detail": "You are not a part of this conversation"},
            #                 status=status.HTTP_403_FORBIDDEN)
        serializer.save(sender=self.request.user)
        
    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)