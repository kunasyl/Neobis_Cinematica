from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieView.as_view()),
    path('soon/', views.SoonMovieView.as_view()),
    path('<int:pk>/', views.RetrieveMovieView.as_view()),
    path('<int:pk>/showtimes', views.MovieShowtimesView.as_view()),
]
