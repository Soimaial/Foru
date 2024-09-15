from rest_framework import viewsets
from forum.models import Message
from api.serializers.message_serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
