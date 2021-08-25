LONGEST_KEY = 6

uniqueStarter = "SKWAO"  # used to disambiguate area of screen chords

movements = {  # sections of the screen relative to the center
        "F": (-1, -1),  # 1
        "FP": (0, -1),  # 2
        "P": (1, -1),   # 3
        "FR": (-1, 0),  # 4
        "FRPB": (0, 0), # 5
        "PB": (1, 0),   # 6
        "R": (-1, 1),   # 7
        "RB": (0, 1),   # 8
        "B": (1, 1)     # 9
        }

def lookup(strokes):
    if strokes[0] == '': raise KeyError  # skip half the strokes early
    x = 50
    y = 50
    size = 100
    for stroke in strokes:
        if not stroke.startswith(uniqueStarter): raise KeyError  # ignore non area of screen commands
        position = stroke[len(uniqueStarter):]  # remove the uniqueStarter
        if position == '': break  # if no selection is made, use the current one
        (xd, yd) = movements[position]  # extract movement 
        xd = size * (xd * (1/3))  # calculate x difference
        yd = size * (yd * (1/3))  # calculate y difference
        x = x + xd
        y = y + yd
        size = size / 3  # adjust size for next movement 
    return("{PLOVER:mouse_set:" + str(int(x)) + "%," + str(int(y)) + "%}")  # return the plover command, with added "%" symbols

