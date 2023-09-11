from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from home.models import HitterReport, HitterStats, PitcherReport, PitcherStats
import requests
from django.utils.dateparse import parse_date
from .utils.mlb_team_utils import get_teams
from .utils.player_utils import get_hitter_stats, get_positions, get_handedness, get_pitch_types, get_pitcher_positions

# Create your views here.
def home(request):
    hitterReports = HitterReport.objects.all()
    pitcherReports = PitcherReport.objects.all()
    template = loader.get_template('home.html')
    context = {
        'hitter_reports': hitterReports,
        'pitcher_reports': pitcherReports
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
            stat='Overall',
            value=data.get('Overall'),
            futurevalue=data.get('fvOverall'),
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
            "hitter_stats": hitter_stats,
        }
        return HttpResponse(template.render(context, request))

def hitter_report_view(request, report_id):
    report = HitterReport.objects.get(id=report_id)
    template = loader.get_template('view_hitter_report.html')
    return HttpResponse(template.render({'report': report}, request))

def hitter_report_edit(request, report_id):
    if request.method == "GET":
        teams=get_teams()
        positions = get_positions()
        handedness = get_handedness()
        hitter_stats = get_hitter_stats()
        report = HitterReport.objects.get(id=report_id)
        context = {
            "teams": teams,
            "positions": positions,
            "handedness": handedness,
            "hitter_stats": hitter_stats,
            "report": report
        }
        print(report.bats)
        template = loader.get_template('edit_hitter_report.html')
        return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        data = request.POST
        date_str = request.POST.get('date')
        date = parse_date(date_str)
        report = HitterReport.objects.get(id=report_id)
        report.firstname=data.get('firstname')
        report.lastname=data.get('lastname')
        report.position=data.get('position')
        report.bats=data.get('bats')
        report.throws=data.get('throws')
        report.date=date
        report.summary=data.get('statement')
        report.team=data.get('team')
        report.save()
        stats = get_hitter_stats()
        for stat in stats:
            print(stat)
            print(data.get(stat))
            print(data.get('fv'+stat))
            print(data.get('comment'+stat))
            stat_obj = report.hitterstats_set.get(stat=stat)
            stat_obj.value=data.get(stat)
            stat_obj.futurevalue=data.get('fv'+stat)
            stat_obj.comment=data.get('comment'+stat)
            stat_obj.save()
        print('here')
        print(data.get('Overall'))
        ovl_stat = report.hitterstats_set.get(stat='Overall')
        ovl_stat.value=data.get('Overall')
        ovl_stat.futurevalue=data.get('fvOverall')
        ovl_stat.save()
        return redirect('/hitter-report/'+str(report_id))

def pitcher_report_add(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        date_str = request.POST.get('date')
        date = parse_date(date_str)
        report = PitcherReport(
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            position=data.get('position'),
            throws=data.get('throws'),
            date=date,
            summary=data.get('statement'),
            team=data.get('team'),
            overall=data.get('Overall'),
            fvoverall=data.get('fvOverall')
        )
        report.save()
        for i in range(1, 5):
            pitch_type = data.get('pitch'+str(i))
            velo_low = data.get('pitch'+str(i)+'-velo-low')
            velo_high = data.get('pitch'+str(i)+'-velo-high')
            value = data.get('pitch'+str(i)+'-grade')
            comment = data.get('pitch'+str(i)+'-comment')
            fv = data.get('pitch'+str(i)+'-fv')
            print(pitch_type)
            print(velo_low)
            print(velo_high)
            print(value)
            print(comment)
            print(fv)
            pitch_obj = PitcherStats(
                player=report,
                pitch_type=pitch_type,
                velo_low=velo_low,
                velo_high=velo_high,
                value=value,
                futurevalue=fv,
                comment=comment
            )
            pitch_obj.save()
        return redirect('home')
    if request.method == "GET":
        teams=get_teams()
        positions = get_pitcher_positions()
        handedness = get_handedness()
        template = loader.get_template('add_pitcher_report.html')
        context = {
            "teams": teams,
            "positions": positions,
            "handedness": handedness,
            "pitch_ids": range(1, 5),
            "pitch_types": get_pitch_types()
        }
        return HttpResponse(template.render(context, request))
