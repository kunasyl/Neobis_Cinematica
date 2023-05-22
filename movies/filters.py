from django_filters import rest_framework as filters

from .models import Movie


class MovieFilter(filters.FilterSet):
    is_active = filters.BooleanFilter(field_name='is_active')
    start_date = filters.DateTimeFilter(field_name='start_date', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='end_date', lookup_expr='lte')

    class Meta:
        model = Movie
        fields = ['is_active', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        kwargs['data']._mutable = True
        if 'is_active' not in kwargs['data']:
            kwargs['data']['is_active'] = True
        kwargs['data']._mutable = True
        super(MovieFilter, self).__init__(*args, **kwargs)

