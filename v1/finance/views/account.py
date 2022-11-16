from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from v1.finance.serializer import account as account_serializer
from v1.finance import models as app_models


class AccountViewSet(ModelViewSet):
    """ViewSet to create and update account"""
    
    permission_classes = (permissions.IsAuthenticated,)
    queryset = app_models.Account.objects.all()
    serializer_class = account_serializer.AccountSerializer
    # http_method_names = ['patch', 'post']

 

