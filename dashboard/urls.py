from django.urls import path, include
from .views import IncomeCategoryData
from rest_framework import routers
from dashboard.views import IncomeCategoryData
from dashboard.views import ExpenseCategoryData
# from app.views import income as income_views
# from app.views import expense as expense_views

router = routers.DefaultRouter()
router.register('MonthlyIncomeData', IncomeCategoryData, basename='income_category')
router.register('MonthlyExpenseData', ExpenseCategoryData, basename='expense_category')

# router.register('income', income_views.IncomeViewSet, basename='income')
# router.register('incomelist', income_views.IncomeListViewSet, basename='income list')

# router.register('expense', expense_views.ExpenseViewSet, basename='expense')
# router.register('expenselist', expense_views.ExpenseListViewSet, basename='expense list')

urlpatterns = [
    # path('',IncomeCategoryData.as_view()),
    path('',include(router.urls)),
]
