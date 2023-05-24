
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('cinemas/', include('cinemas.urls')),
    path('movies/', include('movies.urls')),
    path('showtimes/', include('showtimes.urls')),
]
