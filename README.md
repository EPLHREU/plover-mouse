# Mouse

> Plover plugin for controlling your mouse/cursor with just steno chords

# this is WIP that is half complete

## area-of-screen.py

This will recursively cut the screen into 3x3 sections, using F, R, P, B in combinations to select the 3x3 grid you can move the mouse cursor exactly where you want to.

| section | key  | position      |
| ------- | ---- | ------------- |
| 1       | F    | top left      |
| 2       | FP   | top middle    |
| 3       | P    | top right     |
| 4       | FR   | middle left   |
| 5       | FRPB | middle middle |
| 6       | PB   | middle right  |
| 7       | R    | bottom right  |
| 8       | RB   | bottom middle |
| 9       | B    | bottom right  |

When you have selected an area of the screen, your next movement command will occur within that selected section, as if it was the whole size of the screen.
Your cursor is placed in the center of the area you select.
