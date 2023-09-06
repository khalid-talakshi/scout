from django import template
from django.db.models import Case, When, Value, CharField
from home.utils.mlb_team_utils import get_teams

register = template.Library()

@register.filter(name='team_id_to_code')
def team_id_to_code(team_id):
    teams = get_teams()
    for team in teams:
        if team['id'] == team_id:
            return team['code']
    return 'Unknown'
