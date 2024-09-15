from rest_framework import viewsets
from forum.models import Topic
from api.serializers.topic_serializers import TopicSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
