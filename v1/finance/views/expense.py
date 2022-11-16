from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from v1.finance.serializer import expense as expense_serializer
from v1.finance import models as app_models
from v1.finance import filters as app_filters


class ExpenseViewSet(ModelViewSet):
    """Viewset to create expense"""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = app_models.Expense.objects.all()
    serializer_class = expense_serializer.ExpenseSerializer
    http_method_names = ['post']


class ExpenseListViewSet(ModelViewSet):
    """Viewset to view list of expenses and update them"""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = app_models.Expense.objects.all()
    serializer_class = expense_serializer.ExpenseSerializer
    filterset_class = app_filters.ExpenseFilter

    def get_queryset(self):
        """queryset to get loggin user expense data"""
        
        return app_models.Expense.objects.filter(user=self.request.user.id)
