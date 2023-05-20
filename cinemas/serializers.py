from rest_framework import serializers

from . import models


class CinemaSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Cinema
        fields = ('id', 'name', 'address', 'city', 'schedule')
        depth = 1
