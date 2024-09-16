from rest_framework import viewsets
from forum.models import Message
from api.serializers.message_serializers import MessageSerializer
from api.permissions import PreventPutAndDelete


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [PreventPutAndDelete]
