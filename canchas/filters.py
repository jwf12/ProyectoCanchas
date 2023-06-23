import django_filters
from .models import Shift

class SearchFilter(django_filters.FilterSet):    
    class Meta:
        model = Shift
        fields = [
        'day_shift'
        ]