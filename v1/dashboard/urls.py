from django.urls import path, include
from rest_framework import routers

from .views import IncomeCategoryData
from .views import ExpenseCategoryData
from .views import TotalBalance

router = routers.DefaultRouter()
router.register('MonthlyIncomeData', IncomeCategoryData,
                basename='income_category')
router.register('MonthlyExpenseData', ExpenseCategoryData,
                basename='expense_category')
router.register('TotalBalance', TotalBalance, basename='total_balance')

urlpatterns = [
    path('', include(router.urls)),
]
