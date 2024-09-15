from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.viewsets.forum_viewsets import ForumViewSet
from api.viewsets.topic_viewsets import TopicViewSet
from api.viewsets.message_viewsets import MessageViewSet

router = DefaultRouter()
router.register(r'forums', ForumViewSet, basename='forums')
router.register(r'topics', TopicViewSet, basename='topics'),
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]
