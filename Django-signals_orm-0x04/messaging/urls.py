from django.urls import path, include
from rest_framework import routers
from .views import MessageViewSet, NotificationViewSet, MessageHistoryViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'messagehistories', MessageHistoryViewSet, basename='messagehistory')

urlpatterns = [
    path('', include(router.urls))
]