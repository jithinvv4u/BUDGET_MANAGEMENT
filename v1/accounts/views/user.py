from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from v1.accounts.models import User
from v1.accounts.serializer import user as user_serializer
from v1.accounts import permissions as app_permissions


class UserViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = user_serializer.UserSerializer
    # http_method_names = ['get', 'patch','put']
