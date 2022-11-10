from rest_framework.viewsets import ModelViewSet
from app import models as app_models
from app.serializer import account as account_serializer
from rest_framework import permissions


class AccountViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = app_models.Account.objects.all()
    serializer_class = account_serializer.AccountSerializer
    # http_method_names = ['patch', 'post']

 

