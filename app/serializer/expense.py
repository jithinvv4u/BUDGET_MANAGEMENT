from rest_framework import serializers
from app.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta info."""

        model = Expense
        fields = ['account_type','expense_date','expense_category','expense_amount','expense_note']
