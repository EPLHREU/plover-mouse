import pyautogui as pyag

# Global settings for mouse delay and easing function (tween)
mouse_move_delay_seconds = 0.150
mouse_move_tween_function = pyag.easeInQuad

def pargs(arg, defaults):  # process arguments, use default argument and format correctly
    args = arg.split(",")
    args = (args + len(defaults) * [''])[:len(defaults)]  # pad args to same length as defaults
    ret = []
    for x in range(len(defaults)):
        if args[x] == '':
            ret.append(defaults[x])
        else:
            ret.append(args[x])
    return tuple(ret)

def click(steno, args):  # clicking the mouse
    (button, count, mod1, mod2, mod3, mod4) = pargs(args, ('left', 1, '', '', '', ''))  # default to 1 left click press
    pyag.click(button=button, clicks=int(count))

def move(steno, args):  # move relative to the current position 
    (x, y) = pargs(args, (0, 0))  # default to no movement

    if isinstance(x, str) and x.endswith('%'):  # support percentage movement based off of screen dimensions
        (xs, _) = pyag.size()
        x = xs * (int(x[:-1]) / 100)
    if isinstance(y, str) and y.endswith('%'):
        (_, ys) = pyag.size()
        y = ys * (int(y[:-1]) / 100)

    pyag.move(int(x), int(y), mouse_move_delay_seconds, tween=mouse_move_tween_function)

def set(steno, args):  # set mouse to exact position 
    (x, y) = pargs(args, ('50%', '50%'))  # default to middle of screen 

    if isinstance(x, str) and x.endswith('%'):  # support percentage movement based off of screen dimensions
        (xs, _) = pyag.size()
        x = xs * (int(x[:-1]) / 100)
    if isinstance(y, str) and y.endswith('%'):
        (_, ys) = pyag.size()
        y = ys * (int(y[:-1]) / 100)

    pyag.moveTo(int(x), int(y), mouse_move_delay_seconds, tween=mouse_move_tween_function)

def scroll(steno, args):  # scroll the mouse wheel in any cardinal direction
    (y, x) = pargs(args, (0, 0))  # default to no movement
    pyag.scroll(int(x))
    pyag.hscroll(int(y))

def down(steno, args):  # press and keep a mouse button down
    (button) = pargs(args, ('left'))  # default to left mouse button
    pyag.mouseDown(button=button)

def up(steno, args):  # release a held down mouse button
    (button) = pargs(args, ('left'))  # default to left mouse button
    pyag.mouseUp(button=button)

