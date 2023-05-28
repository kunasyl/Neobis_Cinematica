from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import Http404
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import serializers, services, models, permissions
from showtimes.permissions import IsTicketOwner
from showtimes import models as showtimes_models
from showtimes.choices import TicketStatuses


class UserViewSet(ViewSet):
    user_services: services.UserServicesInterface = services.UserServicesV1()

    def create_user(self, request, *args, **kwargs):
        serializer = serializers.CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        models.Discount.objects.create(
            user_id=request.user
        )

        self.user_services.create_user(data=serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create_token(self, request, *args, **kwargs):
        serializer = serializers.CreateTokenSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        tokens = self.user_services.create_token(data=serializer.validated_data)
        return Response(tokens)


class FeedbackView(ListCreateAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer
    ordering = ('-created_at',)

    def get_permissions(self):
        return permissions.IsFeedbackUser(),


class CreateFeedbackView(APIView):
    permission_classes = (permissions.IsFeedbackUser,)

    def post(self, request, *args, **kwargs):
        context = {
            'user_id': request.user.id
        }

        serializer = serializers.FeedbackSerializer(data=request.data, context=context)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success": "Feedback created successfully"})

        return Response(serializer.errors)


