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
