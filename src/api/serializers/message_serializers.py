from rest_framework import serializers
from forum.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'topic', 'content', 'created_at']
