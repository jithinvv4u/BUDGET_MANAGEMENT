from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta info."""

        model = User
        fields = '__all__'  # ['id', 'name', 'phone', 'dob', ]
