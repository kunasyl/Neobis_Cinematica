from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowtimeView.as_view(), name='showtimes'),
    path('<int:pk>/', views.RetrieveShowtimeView.as_view(), name='showtime'),
    # path('<int:pk>/rooms/', views.ShowtimeRoomsView.as_view(), name='rooms'),
    # path('<int:pk>/rooms/<in:room_id>/', views.RetrieveRoom.as_view(), name='room'),
    path('<int:pk>/tickets/', views.TicketView.as_view(), name='create_ticket'),
    path('<int:pk>/tickets/create/', views.CreateTicketView.as_view(), name='create_ticket'),
]
