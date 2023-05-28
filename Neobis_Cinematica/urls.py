
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('cinemas/', include('cinemas.urls')),
    path('movies/', include('movies.urls')),
    path('', include('showtimes.urls')),
]
