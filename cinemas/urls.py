from django.urls import path

from . import views

urlpatterns = [
    path('', views.CinemaViewSet.as_view({'get': 'list'}))
]
