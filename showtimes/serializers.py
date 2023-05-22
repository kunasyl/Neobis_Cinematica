from rest_framework import serializers

from . import models


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


class TicketSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)


    class Meta:
        model = models.Ticket
        fields = ('id', 'showtime_id', 'seat_id', 'price_age', 'user_id', ' status')

    def create(self, validated_data):
        """
        Create a ticket with additionally creating a seat.
        """
        ticket_data = validated_data.pop('seat_id')

        order_items_data = validated_data.pop('order_items')
        order = models.Order.objects.create(**validated_data)
        for order_item_data in order_items_data:
            order_item_data.pop('order_id', None)
            models.OrderItem.objects.create(order_id=order, **order_item_data)

        return order

