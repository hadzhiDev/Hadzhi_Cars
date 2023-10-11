import django_filters
from django import forms
from apps.models import Brand, Car


class CarFilter(django_filters.FilterSet):

    data_range = django_filters.DateRangeFilter(field_name='date')
    # brands = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Car
        fields = ('brand',)