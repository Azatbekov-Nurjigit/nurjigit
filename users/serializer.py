from abc import ABC

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class UserValidateSerializer(serializers.Serializer, ABC):
    username = serializers.CharField()
    password = serializers.CharField()

class UserCreateSerializer(UserValidateSerializer, ABC):
    @staticmethod
    def validate_username(username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')



