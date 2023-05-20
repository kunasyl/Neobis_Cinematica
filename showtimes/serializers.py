from rest_framework import serializers

from . import models


class ShowtimeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    movie_id = serializers.IntegerField()
    date = serializers.DateTimeField()
    room_id = serializers.IntegerField()
    cinema_id = serializers.IntegerField()
    price_adult = serializers.DecimalField(max_digits=8, decimal_places=2)
    price_child = serializers.DecimalField(max_digits=8, decimal_places=2)
    price_student = serializers.DecimalField(max_digits=8, decimal_places=2)
    price_vip = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = models.Movie
        fields = ('id', 'movie_id', 'date', 'room_id', 'cinema_id',
                  'price_adult', 'price_child', 'price_student', 'price_vip')
        depth = 1

