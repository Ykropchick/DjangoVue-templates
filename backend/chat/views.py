from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Room, Message
from .serializer import RoomSerializer, MessageSerializer

from rest_framework.views import APIView


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessagesViewSet(APIView):
    def get(self, request, *args, **kwargs):
        messages = Message.objects.filter(room__name=self.kwargs['room_name'])
        serializer = MessageSerializer(messages, many=True)
        print(serializer.data)
        return Response(serializer.data)