from rest_framework import serializers
from v1.finance.models import Income


class IncomeSerializer(serializers.ModelSerializer):
    """Serializer for Income."""

    class Meta:
        """Meta info."""

        model = Income
        fields = ['account_type', 'income_date',
                  'income_category', 'income_amount', 'income_note']

    def save(self, **kwargs):
        """save income details with current login user"""
        
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)
