from libqtile import widget

from styles import NEW_COLORTHEME
from widgets.decorations import decoration
from qtile_extras.widget.decorations import *


clock_widget = widget.Clock(
    foreground=NEW_COLORTHEME["light_gray"],
    background=NEW_COLORTHEME["dark_gray"],
    
    format="%d %b | %I:%M %p",
    
)

date_widget = widget.Clock(
    foreground=NEW_COLORTHEME["dark_gray"],
    background=NEW_COLORTHEME["red"],
    format="%d %b",
) 