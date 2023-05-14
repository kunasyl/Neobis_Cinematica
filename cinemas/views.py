from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from cinemas import models, serializers


class CinemaViewSet(ModelViewSet):
    order = models.Cinema

    serializer_class = serializers.CinemaSerializer
    queryset = models.Cinema.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        wrapped_data = {'cinemas': serializer.data}

        return Response(wrapped_data)
