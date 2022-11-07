from rest_framework.viewsets import ModelViewSet
from accounts.models import User
from accounts.serializer import auth as auth_serializer


class SignupViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = auth_serializer.SignupSerializer
    http_method_names = ['post']

class loginViewSet(ModelViewSet):
    serializer_class = auth_serializer.LoginSerializer
    http_method_names = ['post']
