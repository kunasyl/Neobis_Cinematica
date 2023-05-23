from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from django.http import Http404
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponseRedirect
from django.urls import reverse

from movies import models, serializers, services
from showtimes import serializers as showtime_serializers
from .filters import MovieFilter


class MovieView(ListCreateAPIView):
    services = services.MovieServices()

    queryset = services.get_movies()
    serializer_class = serializers.MovieSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    ordering = ('-start_date',)
    filterset_class = MovieFilter

    def get_permissions(self):
        if self.request.method == 'GET':
            return []  # No permissions required for GET requests
        else:
            return [IsAdminUser()]

    def post(self, request, *args, **kwargs):
        serializer = serializers.MovieSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            valid_serializer = serializer.save()

            return Response({"success": "Movie '{}' created successfully".format(valid_serializer.id)})

        return Response(serializer.errors)


class SoonMovieView(ListCreateAPIView):
    services = services.MovieServices()

    queryset = services.get_movies().filter(is_active=False)
    serializer_class = serializers.MovieSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    ordering = ('-start_date',)


class RetrieveMovieView(APIView):
    model = models.Movie

    def get(self, request, *args, **kwargs):
        try:
            cinema = self.model.objects.get(pk=kwargs['pk'])
        except self.model.DoesNotExist:
            raise Http404("Такого кинотеатра не существует")
        serializer = serializers.MovieSerializer(cinema)

        return Response(serializer.data)


class MovieShowtimesView(APIView):
    services = services.MovieServices()

    def get(self, request, *args, **kwargs):
        showtimes = self.services.get_movie_showtimes(movie_id=kwargs['pk'])
        serializer = showtime_serializers.ShowtimeSerializer(showtimes, many=True)

        return Response(serializer.data)


def showtime_redirect(request, *args, **kwargs):
    redirect_url = reverse('showtime', args=[kwargs['showtime_id']])
    return HttpResponseRedirect(redirect_url)


