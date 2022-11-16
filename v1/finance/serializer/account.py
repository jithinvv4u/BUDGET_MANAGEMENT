from rest_framework import serializers
from v1.finance.models import Account


class AccountSerializer(serializers.ModelSerializer):
    """Serializer for Account."""

    class Meta:
        """Meta info."""

        model = Account
        fields = ['account_name', 'account_inintial_amt', 'account_type']

    def save(self, **kwargs):
        """save account details with current login user"""

        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)