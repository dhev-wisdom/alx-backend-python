from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsObjOwner(permissions.BasePermission):
    """
    Object-level permission to only allow users to access their own data.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow users to access their own data.
    """
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, get_user_model()):
            return obj == request.user
        return getattr(obj, 'user', None)
    
class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission:
    - Only allow authenticated users.
    - Only allow participants of the conversation to send, view, update, or delete messages.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", 'DELETE', "GET"]:
            if hasattr(obj, 'conversation'):
                return request.user in obj.conversation.participants.all()
            elif hasattr(obj, 'participants'):
                return request.user in obj.participants.all()
            return False