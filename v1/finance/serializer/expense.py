from rest_framework import serializers
from v1.finance.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    """Serializer for Expense."""

    class Meta:
        """Meta info."""

        model = Expense
        fields = ['id', 'account_type', 'expense_date',
                  'expense_category', 'expense_amount', 'expense_note']

    def save(self, **kwargs):
        """save expense details with current login user"""
        
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)
