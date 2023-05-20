from rest_framework import serializers

from . import models


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField()
    genre = serializers.MultipleChoiceField(choices=models.GENRES)
    age_rate = serializers.IntegerField(max_value=21, min_value=1)
    rating = serializers.FloatField(max_value=10, min_value=1)

    class Meta:
        model = models.Movie
        fields = ('id', 'title', 'genre', 'age_rate', 'rating')
        depth = 1

