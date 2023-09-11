from django import template
from django.db.models import Case, When, Value, CharField
from home.utils.mlb_team_utils import get_teams

register = template.Library()

@register.filter(name='get_overall_stat')
def get_overall_stat(report):
    return {'value': report.overall, 'futurevalue': report.fvoverall}
