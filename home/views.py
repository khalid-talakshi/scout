from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from home.models import HitterReport, HitterStats
import requests
from django.utils.dateparse import parse_date

def map_function(x):
    return {'name': x['name'], 'id': x['id'], 'code': x['abbreviation']}

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

def get_hitter_stats():
    return ['Hit', 'Power', 'Run', 'Fielding', 'Throwing']

def get_positions():
    positions = [
        'P',
        'C',
        '1B',
        '2B',
        '3B',
        'SS',
        'CF',
        'LF',
        'RF',
        'DH'
    ]
    positions.sort()
    return positions

def get_handedness():
    return ["L", "R"]

# Create your views here.
def home(request):
    reports = HitterReport.objects.all()
    template = loader.get_template('home.html')
    print(reports[0].hitterstats_set.filter(stat='Hit')[0].value)
    context = {
        'reports': reports
    }
    return HttpResponse(template.render(context, request))

def hitter_report_add(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        date_str = request.POST.get('date')
        date = parse_date(date_str)
        report = HitterReport(
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            position=data.get('position'),
            bats=data.get('bats'),
            throws=data.get('throws'),
            date=date,
            summary=data.get('statement'),
            team=data.get('team')
        )
        report.save()
        stats = get_hitter_stats()
        for stat in stats:
            print(stat)
            print(data.get(stat))
            print(data.get('fv'+stat))
            print(data.get('comment'+stat))
            stat_obj = HitterStats(
                player=report,
                stat=stat,
                value=data.get(stat),
                futurevalue=data.get('fv'+stat),
                comment=data.get('comment'+stat)
            )
            stat_obj.save()
        ovl_stat = HitterStats(
            player=report,
            stat='overall',
            value=data.get('overall'),
            futurevalue=data.get('fvoverall'),
        )
        ovl_stat.save()
        return redirect('home')
    elif request.method == 'GET':
        teams=get_teams()
        positions = get_positions()
        handedness = get_handedness()
        hitter_stats = get_hitter_stats()
        template = loader.get_template('add_hitter_report.html')
        context = {
            "teams": teams,
            "positions": positions,
            "handedness": handedness,
            "hitter_stats": hitter_stats
        }
        return HttpResponse(template.render(context, request))
