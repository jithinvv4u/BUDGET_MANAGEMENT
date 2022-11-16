from rest_framework import serializers
from v1.accounts.models import User


class SignupSerializer(serializers.ModelSerializer):
    """Serializer to create user."""

    class Meta:
        model = User
        fields = ['name', 'phone_number', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    # def update(self, instance, validated_data):
    #     if 'password' in validated_data.keys():
    #         instance.set_password(validated_data['password'])
    #         instance.save()
    #     return super().update(instance, validated_data)


# class LoginSerializer(serializers.Serializer):
#     """Serializer to login."""

#     phone_number = serializers.CharField()
#     password = serializers.CharField()

#     def create(self, validated_data):
#         """Overriding the create method."""
#         user = authenticate(request=self.context.get('request'),
#             phone_number=validated_data['phone_number'],
#             password=validated_data['password'])
#         if not user:
#             raise UnauthorizedAccess('Invalid phone number or password')

#         return user
