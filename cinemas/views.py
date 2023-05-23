from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse

from cinemas import models, serializers, services
from showtimes import serializers as showtime_serializers


class CinemaView(APIView):
    services = services.CinemaServices()

    def get(self, request, *args, **kwargs):
        cinemas = self.services.get_cinemas()
        serializer = serializers.CinemaSerializer(cinemas, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.CinemaSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            valid_serializer = serializer.save()

            return Response({"success": "Cinema '{}' created successfully".format(valid_serializer.id)})

        return Response(serializer.errors)


class RetrieveCinemaView(APIView):
    model = models.Cinema

    def get(self, request, *args, **kwargs):
        try:
            cinema = self.model.objects.get(pk=kwargs['pk'])
            print('cinema', cinema)
        except self.model.DoesNotExist:
            raise Http404("Такого кинотеатра не существует")
        serializer = serializers.CinemaSerializer(cinema)

        return Response(serializer.data)


class CinemaShowtimesView(APIView):
    services = services.CinemaServices()

    def get(self, request, *args, **kwargs):
        showtimes = self.services.get_cinema_showtimes(cinema_id=kwargs['pk'])
        serializer = showtime_serializers.ShowtimeSerializer(showtimes, many=True)

        return Response(serializer.data)


def showtime_redirect(request, *args, **kwargs):
    redirect_url = reverse('showtime', args=[kwargs['showtime_id']])
    return HttpResponseRedirect(redirect_url)
