from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
from decimal import Decimal
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Sum

from . import models, serializers, permissions, choices
from users.models import Discount


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
            tickets = models.Ticket.objects.filter(
                user_id=request.user,
                status=choices.TicketStatuses.Reserved
            )
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


class PurchaseView(APIView):
    model = models.PurchaseHistory
    permission_classes = (permissions.IsTicketOwner,)

    def get(self, request, *args, **kwargs):
        try:
            purchases = self.model.objects.filter(user_id=request.user)
        except self.model.DoesNotExist:
            raise Http404("У вас нет покупок.")
        serializer = serializers.PurchaseSerializer(purchases, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        Create Purchase.
        """
        tickets = models.Ticket.objects.filter(
            user_id=request.user,
            status=choices.TicketStatuses.Reserved
        )

        for ticket in tickets:
            context = {
                'ticket_id': ticket.id,
            }
            serializer = serializers.PurchaseSerializer(data=request.data, context=context)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                ticket.status = choices.TicketStatuses.Bought
                ticket.save()
            #     return Response({"success": "Purchase created successfully"})

            # return Response(serializer.errors)

        redirect_url = reverse('purchases')
        return HttpResponseRedirect(redirect_url)


