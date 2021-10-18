from django_filters.filterset import FilterSet

from rabbit import models


class ProductFilterSet(FilterSet):
    class Meta:
        model = models.Product
        fields = {
            'title': ['iexact', 'contains'],
            'article': ['iexact', 'icontains'],
            'created_at': ['iexact', 'year__gte'],
            'updated_at': ['iexact', 'year__gte']
        }
