from django.shortcuts import render
from rest_framework import viewsets
from app import models as app_models
import datetime
from django.db.models import Sum, F
from app.serializer.income import IncomeSerializer
from rest_framework.response import Response
# Create your views here.


class IncomeCategoryData(viewsets.ViewSet):
    """Category wise Income related statistical data return this api."""

    def list(self, request):
        today = datetime.date.today()
        total = app_models.Income.objects.aggregate(Sum('income_amount'))
        Income_data = app_models.Income.objects.filter(income_date__year=today.year, income_date__month=today.month).values(
            'income_category').annotate(Sum('income_amount'), percent=F('income_amount__sum') / total['income_amount__sum'] * 100)
        return Response(Income_data)


class ExpenseCategoryData(viewsets.ViewSet):
    """Category wise Expense related statistical data return this api."""

    def list(self, request):
        today = datetime.date.today()
        total = app_models.Expense.objects.aggregate(Sum('expense_amount'))
        Expense_data = app_models.Expense.objects.filter(expense_date__year=today.year, expense_date__month=today.month).values(
            'expense_category').annotate(Sum('expense_amount'), percent=F('expense_amount__sum') / total['expense_amount__sum'] * 100)
        return Response(Expense_data)
