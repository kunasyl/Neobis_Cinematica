from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from cinemas import models, serializers, services


class CinemaView(APIView):
    services = services.CinemaServices()

    def get(self, request, *args, **kwargs):
        cinemas = self.services.get_cinemas()
        serializer = serializers.CinemaSerializer(cinemas, many=True)

        return Response(serializer.data)


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
