from django.urls import path

from . import views

urlpatterns = [
    path('', views.CinemaView.as_view()),
    path('<int:pk>/', views.RetrieveCinemaView.as_view()),
    path('<int:pk>/showtimes/', views.CinemaShowtimesView.as_view()),
    path('<int:pk>/showtimes/<int:showtime_id>/', views.showtime_redirect),
]
