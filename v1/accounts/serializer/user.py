from rest_framework import serializers
from v1.accounts.models import User
from v1.accounts import fields as custom_fields


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user."""

    id = custom_fields.IdencodeField(read_only=True)

    class Meta:
        """Meta info."""

        model = User
        fields = ['id', 'name', 'phone_number',
                  'password', 'profile_image', 'dob', 'monthly_budget']
