from rest_framework import serializers

from . import models


class CinemaSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Cinema
        fields = ('id', 'name', 'address', 'city', 'schedule')
        depth = 1


class SeatSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = models.Seat
        fields = ('id', 'room_id', 'row', 'seat', 'is_vip', )
