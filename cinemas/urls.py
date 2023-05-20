from django.urls import path

from . import views

urlpatterns = [
    path('', views.CinemaView.as_view()),
    path('<int:pk>/', views.RetrieveCinemaView.as_view()),
]
