from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import models, serializers, permissions


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


class TicketView(APIView):
    permission_classes = (permissions.IsTicketOwner, )

    def get(self, request, *args, **kwargs):
        try:
            tickets = models.Ticket.objects.filter(user_id=request.user)
        except models.Ticket.DoesNotExist:
            raise Http404("У вас нет билетов")
        serializer = serializers.RetrieveTicketSerializer(tickets, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Create ticket for reservation only.
        """
        context = {
            'showtime_id': kwargs['pk'],
            'user_id': request.user.id
        }

        if isinstance(request.data, list):
            serializer = serializers.CreateTicketSerializer(data=request.data, many=True, context=context)
        else:
            serializer = serializers.CreateTicketSerializer(data=request.data, context=context)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # request.session['tickets'] = serializer.data
            redirect_url = reverse('tickets', args=[kwargs['pk']])

            return HttpResponseRedirect(redirect_url)
            # return Response(serializer.data)

        return Response(serializer.errors)

    def put(self, request, *args, **kwargs):
        """
        Updates status of ticket to buy.
        """
        ticket = models.Ticket.objects.get(id=request.data.get('id'))
        if isinstance(request.data, list):
            serializer = serializers.UpdateTicketSerializer(ticket, data=request.data, many=True)
        else:
            serializer = serializers.UpdateTicketSerializer(ticket, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



