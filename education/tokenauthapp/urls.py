from django.urls import path, include
# from .views import AuthView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #  path('', AuthView.as_view()),
    path('token/', views.obtain_auth_token),
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('o2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
