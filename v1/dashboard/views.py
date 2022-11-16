from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Sum, F
import datetime

from v1.finance.serializer.income import IncomeSerializer
from v1.finance import models as app_models
# Create your views here.


class IncomeCategoryData(viewsets.ViewSet):
    """Category wise Income related statistical data return this api."""

    def list(self, request):
        user_id = self.request.user.id
        today = datetime.date.today()
        total = app_models.Income.objects.filter(
            user=user_id).aggregate(Sum('income_amount'))
        Income_data = app_models.Income.objects.filter(user=user_id, income_date__year=today.year, income_date__month=today.month).values(
            'income_category').annotate(Sum('income_amount'), percent=F('income_amount__sum') / total['income_amount__sum'] * 100)
        return Response(Income_data)


class ExpenseCategoryData(viewsets.ViewSet):
    """Category wise Expense related statistical data return this api."""

    def list(self, request):
        user_id = self.request.user.id
        today = datetime.date.today()
        total = app_models.Expense.objects.filter(
            user=user_id).aggregate(Sum('expense_amount'))
        Expense_data = app_models.Expense.objects.filter(user=user_id, expense_date__year=today.year, expense_date__month=today.month).values(
            'expense_category').annotate(Sum('expense_amount'), percent=F('expense_amount__sum') / total['expense_amount__sum'] * 100)
        return Response(Expense_data)


class TotalBalance(viewsets.ViewSet):
    """Category wise Expense related statistical data return this api."""

    def list(self, request):
        user_id = self.request.user.id
        initial = app_models.Account.objects.filter(
            user=user_id).aggregate(Sum('account_inintial_amt'))
        income = app_models.Income.objects.filter(
            user=user_id).aggregate(Sum('income_amount'))
        expense = app_models.Expense.objects.filter(
            user=user_id).aggregate(Sum('expense_amount'))
        print(income['income_amount__sum'])
        print(expense['expense_amount__sum'])
        print(initial['account_inintial_amt__sum'])
        balance = income['income_amount__sum'] - \
            expense['expense_amount__sum'] + \
            initial['account_inintial_amt__sum']
        return Response(balance)
