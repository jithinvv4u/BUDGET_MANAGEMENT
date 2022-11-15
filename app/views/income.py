from app.serializer import income as income_serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from app import models as app_models
from app import filters as app_filters


class IncomeViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = app_models.Income.objects.all()
    serializer_class = income_serializer.IncomeSerializer
    http_method_names = ['post']


class IncomeListViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = income_serializer.IncomeSerializer
    http_method_names = ['get', 'patch']
    filterset_class = app_filters.IncomeFilter

    def get_queryset(self):
        return app_models.Income.objects.filter(user=self.request.user.id)
