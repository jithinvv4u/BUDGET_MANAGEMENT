from django.urls import path, include
from rest_framework import routers
from accounts.views import user as user_views
from accounts.views import auth as auth_views

router = routers.DefaultRouter()
router.register('user', user_views.UserViewSet)
router.register('signup', auth_views.SignupViewSet,basename='signup')
router.register('login', auth_views.loginViewSet,basename='login')

urlpatterns = [
    path('', include(router.urls)),
]
