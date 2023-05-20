from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from movies import models, serializers, services
from showtimes import serializers as showtime_serializers


class MovieView(APIView):
    services = services.MovieServices()

    def get(self, request, *args, **kwargs):
        movies = self.services.get_cinemas()
        serializer = serializers.MovieSerializer(movies, many=True)

        return Response(serializer.data)


class RetrieveMovieView(APIView):
    model = models.Movie

    def get(self, request, *args, **kwargs):
        try:
            cinema = self.model.objects.get(pk=kwargs['pk'])
            print('cinema', cinema)
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


