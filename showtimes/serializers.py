from rest_framework import serializers

from . import models, choices
from cinemas import models as cinemas_models
from users import models as users_models


class ShowtimeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # sold_tickets_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Showtime
        fields = ('id', 'movie_id', 'date', 'room_id', 'cinema_id', 'tickets_sold',
                  'price_adult', 'price_child', 'price_student', 'price_vip')
        # depth = 1

    # def get_sold_tickets_count(self, obj):
    #     return obj.showtime_tickets.count()


class RetrieveTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ('id', 'showtime_id', 'seat_id', 'price_age', 'user_id', 'status')
        # depth = 1


class CreateTicketSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    showtime_id = serializers.IntegerField(source='showtime.id', read_only=True)
    seat_id = serializers.IntegerField(source='seat.id', read_only=True)
    row = serializers.IntegerField(write_only=True)
    place = serializers.IntegerField(write_only=True)
    price_age = serializers.ChoiceField(choices=choices.PriceAges.choices)
    user_id = serializers.UUIDField(source='user.id', read_only=True)
    status = serializers.ChoiceField(choices=choices.TicketStatuses.choices, read_only=True)

    class Meta:
        model = models.Ticket
        fields = ('id', 'showtime_id', 'seat_id', 'price_age', 'user_id', 'status', 'row', 'place',)

    def create(self, validated_data):
        """
        Create a ticket with additionally creating a seat for reserving only.
        """
        showtime_id = self.context.get('showtime_id')
        showtime = models.Showtime.objects.get(id=showtime_id)
        showtime.tickets_sold += 1
        showtime.save()

        room_id = showtime.room_id
        row = validated_data.pop('row', None)
        place = validated_data.pop('place', None)
        seat = cinemas_models.Seat(room_id=room_id, row=row, place=place)
        seat.save()

        user_id = self.context.get('user_id')
        user = users_models.User.objects.get(id=user_id)

        ticket = models.Ticket.objects.create(
            showtime_id=showtime,
            seat_id=seat,
            price_age=validated_data.pop('price_age'),
            user_id=user,
            **validated_data
        )

        return ticket


class UpdateTicketSerializer(serializers.ModelSerializer):
    """
    Used for updating status of ticket and creates Purchase.
    """
    id = serializers.UUIDField(read_only=True)
    showtime_id = serializers.IntegerField(read_only=True)
    seat_id = serializers.IntegerField(read_only=True)
    price_age = serializers.ChoiceField(choices=choices.PriceAges.choices, read_only=True)
    user_id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Ticket
        fields = ('id', 'showtime_id', 'seat_id', 'price_age', 'user_id', 'status')

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance
