from .models import PCS
import django_filters



class PCSfilters(django_filters.FilterSet):
    Processor = django_filters.CharFilter(lookup_expr="icontains")
    graphics_card = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = PCS
        fields = ['Processor', 'graphics_card']
        

