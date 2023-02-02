from rest_framework import serializers
from .models import Room, Message
from UserExtends.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone']


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['room', 'text', 'user']


class RoomSerializer(serializers.ModelSerializer):
    current_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['name', 'current_users']
        many = True
