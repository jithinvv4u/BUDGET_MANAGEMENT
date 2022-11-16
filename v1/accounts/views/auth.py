from rest_framework.viewsets import ModelViewSet

from v1.accounts.models import User
from v1.accounts.serializer import auth as auth_serializer


class SignupViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = auth_serializer.SignupSerializer
    http_method_names = ['post']

# class loginViewSet(ModelViewSet):
#     serializer_class = auth_serializer.LoginSerializer
#     authentication_classes = (authentication.TokenAuthentication, )
#     http_method_names = ['post']
