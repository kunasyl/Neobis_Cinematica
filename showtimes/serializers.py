from rest_framework import serializers
from decimal import Decimal

from . import models, choices, services
from cinemas import models as cinemas_models
from users import models as users_models

services = services.ShowtimeServices()


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
    price = serializers.SerializerMethodField()
    # total_price = serializers.SerializerMethodField()

    class Meta:
        model = models.Ticket
        fields = ('id', 'showtime_id', 'seat_id', 'price_age', 'user_id', 'status', 'price')
        # depth = 1

    def get_price(self, obj):
        """
        Calculates ticket price.
        """
        price = services.get_price(obj=obj)

        return price


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


class PurchaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    ticket_id = serializers.UUIDField(source='purchasehistory.ticket_id', read_only=True)
    pay_status = serializers.MultipleChoiceField(choices=choices.PayStatuses.choices, read_only=True)
    user_id = serializers.UUIDField(source='user.id', read_only=True)
    price = serializers.DecimalField(
        source='purchasehistory.price',
        max_digits=8,
        decimal_places=2,
        read_only=True
    )
    discount_added = serializers.DecimalField(
        source='purchasehistory.discount_added',
        max_digits=8,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = models.PurchaseHistory
        # fields = ('id', 'ticket_id', 'pay_status', 'user_id', 'price', 'discount_used', 'discount_added')
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a purchase.
        """
        ticket_id = self.context.get('ticket_id')
        ticket = models.Ticket.objects.get(id=ticket_id)

        user_id = ticket.user_id
        user = models.User.objects.get(id=user_id.id)
        price = services.get_price(obj=ticket)

        discount_used = validated_data.pop('discount_used', None)
        discount_used = self.validate_used_discount(user_id=user_id, wanted_discount=discount_used)

        discount_added = self.count_discount(price)

        purchase = models.PurchaseHistory.objects.create(
            ticket_id=ticket,
            user_id=user,
            price=price,
            discount_used=discount_used,
            discount_added=discount_added
        )

        # Update discount of the user
        discount = users_models.Discount.objects.get(user_id=user)
        discount.tickets_bought += 1
        discount.discount_count -= discount_used
        discount.discount_count += discount_added
        discount.save()

        return purchase

    @staticmethod
    def validate_used_discount(user_id, wanted_discount):
        discount = users_models.Discount.objects.get(user_id=user_id.id)
        if wanted_discount <= discount.discount_count:
            return 0
        return wanted_discount

    @staticmethod
    def count_discount(price) -> Decimal:
        return price*Decimal(0.03)
