from django import template
from django.db.models import Case, When, Value, CharField

register = template.Library()

@register.filter(name='order_by_custom_stat')
def order_by_custom_stat(queryset):
    order = ['Hit', 'Power', 'Run', 'Fielding', 'Throwing']
    ordering_conditions = [When(stat=stat, then=Value(order)) for order, stat in enumerate(order)]
    ordering_expression = Case(*ordering_conditions, default=Value(len(order)), output_field=CharField())
    return queryset.annotate(custom_order=ordering_expression).order_by('custom_order')
