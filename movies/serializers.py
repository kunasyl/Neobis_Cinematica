from rest_framework import serializers

from . import models


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    genre = serializers.MultipleChoiceField(choices=models.GENRES)

    class Meta:
        model = models.Movie
        fields = ('id', 'title', 'genre', 'age_rate', 'rating', 'is_active', 'start_date', 'end_date')
        depth = 1

