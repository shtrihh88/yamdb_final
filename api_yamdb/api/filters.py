from django_filters import rest_framework as filters


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='contains'
    )
    category = filters.CharFilter(
        field_name='category__slug',
        lookup_expr='contains'
    )
    year = filters.NumberFilter(field_name='year', lookup_expr='contains')
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        fields = ['genre', 'category', 'year', 'name']
