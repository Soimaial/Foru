from django.urls import path, include
from rest_framework import routers
from api.viewsets.forum_viewsets import ForumViewSet
from api.viewsets.topic_viewsets import TopicViewSet
from api.viewsets.message_viewsets import MessageViewSet

routers = routers.DefaultRouter()
routers.register(r'forums', ForumViewSet, basename='forums')
routers.register(r'topics', TopicViewSet, basename='topics'),
routers.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(routers.urls)),
]
