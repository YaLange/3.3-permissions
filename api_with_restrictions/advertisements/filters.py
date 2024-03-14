from django_filters import rest_framework as filters
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    FILTER_CHOICES = (
        ("OPEN", "Открыто"),
        ("CLOSED", "Закрыто"),)

    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    updated_at = filters.DateFromToRangeFilter(field_name='updated_at')
    status = filters.ChoiceFilter(field_name='status', choices=FILTER_CHOICES)

    class Meta:
        model = Advertisement
        fields = ['created_at', 'updated_at', 'status']
