from django import template
from django.db.models import Case, When, Value, CharField
from home.utils.mlb_team_utils import get_teams

register = template.Library()

@register.filter(name='get_stat_by_name')
def team_id_to_code(queryset, stat_name):
    print('here')
    print(type(queryset))
    return queryset.filter(stat=stat_name)[0]
