from rest_framework import serializers
from app.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta info."""

        model = Account
        fields = ['account_name', 'account_inintial_amt', 'account_type']

    def save(self, **kwargs):
        print(self.context['request'].user)
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)

    # def create(self, validated_data):
    #     user = self.context['request'].user

    #     if user not in validated_data['user']:
    #         validated_data['users'].append(user)
