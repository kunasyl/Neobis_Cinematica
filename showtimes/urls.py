from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowtimeView.as_view(), name='showtimes'),
    path('<int:pk>/', views.RetrieveShowtimeView.as_view(), name='showtime'),
    path('<int:pk>/tickets/', views.TicketView.as_view(), name='tickets'),
    path('<int:pk>/tickets/reserve/', views.TicketView.as_view(), name='reserve_ticket'),
    # path('<int:pk>/tickets/buy/', views.TicketView.as_view(), name='buy_ticket'),
    path('purchases/', views.PurchaseView.as_view(), name='purchases'),
    path('purchases/create/', views.PurchaseView.as_view(), name='create_purchase'),
]
