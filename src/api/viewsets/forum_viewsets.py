from rest_framework import viewsets
from forum.models import Forum
from api.serializers.forum_serializers import ForumSerializer

class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
