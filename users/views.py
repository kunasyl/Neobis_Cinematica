from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from . import serializers, services, models, permissions


class UserViewSet(ViewSet):
    user_services: services.UserServicesInterface = services.UserServicesV1()

    def create_user(self, request, *args, **kwargs):
        serializer = serializers.CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

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
        return permissions.IsTicketOwner(),


class CreateFeedbackView(APIView):
    permission_classes = (permissions.IsTicketOwner,)

    def post(self, request, *args, **kwargs):
        context = {
            'user_id': request.user.id
        }

        serializer = serializers.FeedbackSerializer(data=request.data, context=context)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success": "Feedback created successfully"})

        return Response(serializer.errors)

