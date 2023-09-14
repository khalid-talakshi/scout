from .player_utils import get_hitter_stats

def validate_player_info(data, type):
    """
    Validate a list of forms.
    """
    errors = []
    if data.get('firstname') == '':
        errors.append('First name is required')
    if data.get('lastname') == '':
        errors.append('Last name is required')
    if data.get('position') == '...':
        errors.append('Position is required')
    if data.get('throws') == '...':
        errors.append('Throws is required')
    if type == 'hitter' and data.get('bats') == '...':
        errors.append('Bats is required')
    if data.get('team') == '':
        errors.append('Team is required')
    if data.get('Overall') == '':
        errors.append('Overall is required')
    if data.get('fvOverall') == '':
        errors.append('Future Value Overall is required')
    if data.get('date') == '':
        errors.append('Date is required')
    return errors

def validate_hitter_stats(data):
    errors = []
    for stat in get_hitter_stats():
        if data.get(stat) == '...':
            errors.append(stat+' is required')
        if data.get('fv'+stat) == '...':
            errors.append('Future Value '+stat+' is required')
    return errors

def validate_pitcher_stats(data):
    errors = []
    for i in range(1, 5):
        if data.get('pitch'+str(i)) == '':
            errors.append('Pitch '+str(i)+' type is required')
        if data.get('pitch'+str(i)+'-velo-low') == '':
            errors.append('Pitch '+str(i)+' velocity low is required')
        if data.get('pitch'+str(i)+'-velo-high') == '':
            errors.append('Pitch '+str(i)+' velocity high is required')
        if data.get('pitch'+str(i)+'-grade') == '':
            errors.append('Pitch '+str(i)+' grade is required')
        if data.get('pitch'+str(i)+'-fv') == '':
            errors.append('Pitch '+str(i)+' future value is required')
    return errors
