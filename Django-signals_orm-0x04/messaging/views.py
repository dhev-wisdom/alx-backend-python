from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model
from .serializer import MessageSerializer, NotificationSerializer, MessageHistorySerializer
from .models import Message, Notification, MessageHistory

User = get_user_model()

# Create your views here.
class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class MessageHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer
