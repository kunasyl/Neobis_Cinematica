from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.http import Http404

from . import models, serializers


class ShowtimeView(ListCreateAPIView):
    queryset = models.Showtime.objects.all()
    serializer_class = serializers.ShowtimeSerializer
    ordering = ('-date',)
    permission_classes = (IsAdminUser, )

    def post(self, request, *args, **kwargs):
        serializer = serializers.ShowtimeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            valid_serializer = serializer.save()

            return Response({"success": "Showtime '{}' created successfully".format(valid_serializer.id)})

        return Response(serializer.errors)


class RetrieveShowtimeView(APIView):
    model = models.Showtime

    def get(self, request, *args, **kwargs):
        try:
            showtime = self.model.objects.get(pk=kwargs['pk'])
        except self.model.DoesNotExist:
            raise Http404("Такого сеанса не существует")
        serializer = serializers.ShowtimeSerializer(showtime)

        return Response(serializer.data)


class TicketView(ListAPIView):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.RetrieveTicketSerializer
    ordering = ('-created_at',)
    permission_classes = (IsAdminUser,)


class CreateTicketView(APIView):
    def post(self, request, *args, **kwargs):
        context = {
            'showtime_id': kwargs['pk'],
            'user_id': request.user.id
        }

        if isinstance(request.data, list):
            serializer = serializers.TicketSerializer(data=request.data, many=True, context=context)
        else:
            serializer = serializers.TicketSerializer(data=request.data, context=context)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success": "Ticket(s) created successfully"})

        return Response(serializer.errors)

