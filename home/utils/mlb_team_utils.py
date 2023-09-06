import requests

def map_function(x):
    return {'name': x['name'], 'id': x['id'], 'code': x['abbreviation']}
    try:
        team_request = requests.get('https://statsapi.mlb.com/api/v1/teams?sportId=1')
        team_data = team_request.json()['teams']
        team_objs = list(map(lambda x: map_function(x), team_data))
        team_objs.sort(key=lambda x: x['name'])
        return team_objs
    except Exception as e:
        print('error: get_teams', e)
        return []

def get_teams():
    try:
        team_request = requests.get('https://statsapi.mlb.com/api/v1/teams?sportId=1')
        team_data = team_request.json()['teams']
        team_objs = list(map(lambda x: map_function(x), team_data))
        team_objs.sort(key=lambda x: x['name'])
        return team_objs
    except Exception as e:
        print('error: get_teams', e)
        return []
