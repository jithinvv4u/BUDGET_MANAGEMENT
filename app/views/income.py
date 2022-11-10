from app.serializer import income as income_serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from app import models as app_models
from app import filters as app_filters


class IncomeViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = app_models.Income.objects.all()
    serializer_class = income_serializer.IncomeSerializer
    http_method_names = ['patch', 'post']

class IncomeListViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = app_models.Income.objects.all()
    serializer_class = income_serializer.IncomeSerializer
    http_method_names = ['get']
    filterset_class = app_filters.IncomeFilter
