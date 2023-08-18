from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    date = DateFromToRangeFilter()


    class Meta:
        model = Advertisement
        fields = ['date']
