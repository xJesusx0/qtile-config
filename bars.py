from libqtile import bar
from widgets import TOP_BAR_WIDGETS, BOTTOM_BAR_WIDGETS
from styles import NEW_COLORTHEME

top_bar_size = 32
top_bar_margin = [9,9,0,9]


bottom_bar_size = 32
bottom_bar_margin = [0,9,9,9]


TOP_BAR = bar.Bar(
    TOP_BAR_WIDGETS,
    top_bar_size,
    margin = top_bar_margin,
    background = NEW_COLORTHEME["dark_gray"]
)

BOTTOM_BAR =  bar.Bar(
    BOTTOM_BAR_WIDGETS,
    bottom_bar_size,
    margin = bottom_bar_margin,
    background = NEW_COLORTHEME["red"],
    reserve = True,
)
# You can uncomment this variable if you see that on X11 floating resize/moving is laggy
# By default we handle these events delayed to already improve performance, however your system might still be struggling
# This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
# x11_drag_polling_rate = 60,
