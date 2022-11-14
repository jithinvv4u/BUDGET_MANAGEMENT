from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta info."""

        model = User
        fields = ['id', 'name', 'phone_number',
                  'password', 'profile_image', 'dob']

    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     # user = super().create(validated_data)
    #     user = User(
    #         phone_number=validated_data['phone_number'], email=validated_data['email'])
    #     user.set_password(password)
    #     user.save()
    #     return user
