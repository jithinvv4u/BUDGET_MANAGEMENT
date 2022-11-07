from rest_framework import serializers
from django.contrib.auth import authenticate
from common.exceptions import UnauthorizedAccess
from accounts.models import User


class SignupSerializer(serializers.ModelSerializer):
    """Serializer to create user."""

    class Meta:
        model = User
        fields = ['name', 'phone', 'password']


class LoginSerializer(serializers.Serializer):
    """Serializer to login."""

    phone_number = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        """Overriding the create method."""
        user = authenticate(
            phone_number=validated_data['phone_number'],
            password=validated_data['password'])
        if not user:
            raise UnauthorizedAccess('Invalid phone number or password')

        return user

    # def to_representation(self, obj):
    #     """Overriding the value returned when returning the
    #     serializer."""
    #     data = {
    #         'token': obj.issue_access_token(),
    #         'id': obj.id,
    #     }
    #     return data
