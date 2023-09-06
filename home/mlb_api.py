import requests

def get_teams():
    team_request = requests.get('https://statsapi.mlb.com/api/v1/teams?sportId=1')
    return team_request.json()['teams']
