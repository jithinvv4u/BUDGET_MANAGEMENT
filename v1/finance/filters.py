import django_filters
from django_filters import rest_framework as filters
from django.db.models import Q

from v1.finance import models as app_models


class IncomeFilter(django_filters.FilterSet):
    # account_type = filters.CharFilter(method='search_filter')
    # income_category = filters.CharFilter(method='search_filter')
    # income_date = filters.CharFilter(method='search_filter')

    class Meta:
        model = app_models.Income
        fields = ('account_type', 'income_category', 'income_date')

    # def search_filter(self, queryset, name, value):
    #     query = Q(account_type__icontains=value) | Q(
    #         income_category__icontains=value) | Q(income_date__icontains=value)
    #     return queryset.filter(query)


class ExpenseFilter(django_filters.FilterSet):
    # account_type = filters.CharFilter(method='search_filter')
    # expense_category = filters.CharFilter(method='search_filter')
    # expense_date = filters.CharFilter(method='search_filter')

    class Meta:
        model = app_models.Expense
        fields = ('account_type__account_type',
                  'expense_category', 'expense_date')

    # def search_filter(self, queryset, name, value):
    #     query = Q(account_type__icontains=value) | Q(
    #         expense_category__icontains=value) | Q(expense_date__icontains=value)
    #     return queryset.filter(query)
