from rest_framework.viewsets import ModelViewSet
from accounts.models import User
from accounts.serializer import user as user_serializer
from rest_framework import permissions
from accounts import permissions as app_permissions


class UserViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # permission_classes = (app_permissions.IsOwnerOrReadOnly, )
    queryset = User.objects.all()
    serializer_class = user_serializer.UserSerializer
    # http_method_names = ['get', 'patch','put']
    
    
