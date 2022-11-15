from rest_framework.viewsets import ModelViewSet
from accounts.models import User
from accounts.serializer import auth as auth_serializer
# from rest_framework import authentication

class SignupViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = auth_serializer.SignupSerializer
    http_method_names = ['post']

# class loginViewSet(ModelViewSet):
#     serializer_class = auth_serializer.LoginSerializer
#     authentication_classes = (authentication.TokenAuthentication, )
#     http_method_names = ['post']
