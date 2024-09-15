from rest_framework import serializers
from forum.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'forum', 'title', 'created_at']
