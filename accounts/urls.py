from django.urls import path, include
from rest_framework import routers
from accounts.views import user as user_views
from accounts.views import auth as auth_views

router = routers.DefaultRouter()
router.register('user', user_views.UserViewSet)
router.register('signup', auth_views.SignupViewSet,basename='signup')
# router.register('login', auth_views.loginViewSet,basename='login')
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('', include(router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
