from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

app_name = 'authentication'
urlpatterns = [
    path('create/', views.UserViewSet.as_view({'post': 'create_user'})),
    path('token/', views.UserViewSet.as_view({'post': 'create_token'})),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]