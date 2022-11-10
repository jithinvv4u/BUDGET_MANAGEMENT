from app.serializer import expense as expense_serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from app import models as app_models
from app import filters as app_filters


class ExpenseViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = app_models.Expense.objects.all()
    serializer_class = expense_serializer.ExpenseSerializer
    http_method_names = ['patch', 'post']

class ExpenseListViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = app_models.Expense.objects.all()
    serializer_class = expense_serializer.ExpenseSerializer
    http_method_names = ['get']
    filterset_class = app_filters.ExpenseFilter
