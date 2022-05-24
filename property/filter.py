import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    title= django_filters.CharFilter(field_name='title',lookup_expr='icontains')   
    price = django_filters.NumberFilter(field_name='price', lookup_expr='gt')


    class Meta:
        model = Property()
        fields = ['title', "place", 'price', 'category']