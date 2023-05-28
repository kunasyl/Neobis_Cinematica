from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

app_name = 'authentication'
urlpatterns = [
    path('create/', views.UserViewSet.as_view({'post': 'create_user'})),
    path('token/create/', views.UserViewSet.as_view({'post': 'create_token'})),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('feedbacks/', views.FeedbackView.as_view(), name='feedbacks'),
    path('feedbacks/create/', views.CreateFeedbackView.as_view(), name='create_feedback'),
]