from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

def map_function(x):
    return {'name': x['name'], 'id': x['id'], 'code': x['abbreviation']}

def get_teams():
    try:
        team_request = requests.get('https://statsapi.mlb.com/api/v1/teams?sportId=1')
        team_data = team_request.json()['teams']
        team_objs = list(map(lambda x: map_function(x), team_data))
        return team_objs
    except Exception as e:
        print('error: get_teams', e)
        return []



# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
