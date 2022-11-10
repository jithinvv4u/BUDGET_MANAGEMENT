from django.urls import path, include
from rest_framework import routers
from app.views import account as account_views
from app.views import income as income_views
from app.views import expense as expense_views

router = routers.DefaultRouter()
router.register('account', account_views.AccountViewSet, basename='account')

router.register('income', income_views.IncomeViewSet, basename='income')
router.register('incomelist', income_views.IncomeListViewSet, basename='income list')

router.register('expense', expense_views.ExpenseViewSet, basename='expense')
router.register('expenselist', expense_views.ExpenseListViewSet, basename='expense list')

urlpatterns = [
    path('', include(router.urls)),
]
