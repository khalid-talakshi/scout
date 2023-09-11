from django import template
from django.db.models import Case, When, Value, CharField
from home.utils.mlb_team_utils import get_teams

register = template.Library()

@register.filter(name='get_pitch_by_name')
def get_pitch_by_name(queryset, pitch_name):
    print('here')
    print(queryset)
    try:
        pitch = queryset.filter(pitch_type=pitch_name)[0]
        return pitch
    except Exception as e:
        return None

