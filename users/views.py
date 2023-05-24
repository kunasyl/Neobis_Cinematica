from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView
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


class PurchaseView(ListAPIView):
    queryset = models.PurchaseHistory.objects.all()
    serializer_class = serializers.PurchaseSerializer
    ordering = ('-created_at',)
    permission_classes = (IsAuthenticated,)


class CreatePurchaseView(APIView):
    """
    Create Purchase.
    """

    # def post(self):
    #     # ('id', 'showtime_id', 'seat_id', 'price_age', 'user_id', 'status')
    #     ticket_data = self.kwargs['serialized_data']
    #     print('ticket_data', ticket_data)
    #
    #     showtime = models.Showtime.objects.get(id=instance.showtime_id)
    #     ticket_id = showtime.r
    #
    #     if instance.status == choices.TicketStatuses.Bought:
    #         purchase = users_models.PurchaseHistory.objects.create(
    #             ticket_id=instance.id,
    #             pay_status=
    #             user_id =
    #         price =
    #         discount_used =
    #         discount_added =
    #         )
    #
    #     redirect_url = reverse('purchases')
    #     return HttpResponseRedirect(redirect_url)

