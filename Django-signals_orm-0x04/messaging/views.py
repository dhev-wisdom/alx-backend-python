from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model
from .serializer import MessageSerializer, NotificationSerializer, MessageHistorySerializer
from .models import Message, Notification, MessageHistory
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
@login_required
def delete_user(request):
    user = request.user()
    user.delete()
    return

def get_thread(message):
    """Recurcively get a message and all it's replies"""
    replies = message.replies.all().select_related("sender", "receiver")
    return {
        "id": message.id,
        "content": message.content,
        "sender": message.sender.username,
        "replies": [get_thread(reply) for reply in replies]
    }

def inbox(request):
    user = request.user
    unread = Message.filter(receiver=user, edited=False).unread_for_user(user)
    return


class UnreadMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Message.unread.unread_for_user(self.request.user)
    

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
