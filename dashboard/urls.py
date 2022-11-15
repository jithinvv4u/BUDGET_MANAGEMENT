from django.urls import path, include
from .views import IncomeCategoryData
from rest_framework import routers
from dashboard.views import IncomeCategoryData
from dashboard.views import ExpenseCategoryData
from dashboard.views import TotalBalance

router = routers.DefaultRouter()
router.register('MonthlyIncomeData', IncomeCategoryData,
                basename='income_category')
router.register('MonthlyExpenseData', ExpenseCategoryData,
                basename='expense_category')
router.register('TotalBalance', TotalBalance, basename='total_balance')

urlpatterns = [
    path('', include(router.urls)),
]
