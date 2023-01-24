from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'time_registrate', 'phone', 'avatar', 'staff', 'admin']