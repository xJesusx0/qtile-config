from libqtile import widget
from libqtile import bar

from styles import NEW_COLORTHEME, ICONS

def get_right_arrow(bg: str = "dark_gray", fg: str = "yellow") -> widget:
    
    custom_bg = NEW_COLORTHEME[bg]
    custom_fg = NEW_COLORTHEME[fg]
    
    right_arrow = widget.TextBox(
        text='',
        font="JetBrainsMono Nerd Font Mono",
        background = custom_bg,
        foreground = custom_fg,
        padding=0,
        fontsize=30,
    )
    
    return right_arrow

def get_left_arrow(bg: str = "dark_gray", fg: str = "yellow") -> widget:
    
    custom_bg = NEW_COLORTHEME[bg]
    custom_fg = NEW_COLORTHEME[fg]
    
    left_arrow = widget.TextBox(
        text='',
        font="JetBrainsMono Nerd Font Mono",
        background = custom_bg,
        foreground = custom_fg,
        padding=0,
        fontsize=30,
    )
    
    return left_arrow

def get_left_diagonal_bar(bg: str = "dark_gray", fg: str = "yellow") -> widget:

    custom_bg = NEW_COLORTHEME[bg]
    custom_fg = NEW_COLORTHEME[fg]
    
    ldb = widget.TextBox(
        text='',
        font="JetBrainsMono Nerd Font Mono",
        background= custom_bg,
        foreground=custom_fg,
        padding=0,
        fontsize=37
    )

    return ldb

def get_right_diagonal_bar(bg: str = "dark_gray", fg: str = "yellow") -> widget:

    custom_bg = NEW_COLORTHEME[bg]
    custom_fg = NEW_COLORTHEME[fg]
    
    rdb = widget.TextBox(
        text='',
        font="JetBrainsMono Nerd Font Mono",
        background= custom_bg,
        foreground=custom_fg,
        padding=0,
        fontsize=37
    )

    return rdb


def get_separator(bg: str = "dark_gray", fg: str = "yellow") -> widget:
    custom_bg = NEW_COLORTHEME[bg]
    custom_fg = NEW_COLORTHEME[fg]
    
    separator = widget.Sep(
        linewidth=0,
        padding=8,
        background=custom_bg,
        foreground=custom_fg
    )

    return separator


def get_spacer(bg: str = "dark_gray") -> widget:
    custom_bg = NEW_COLORTHEME[bg]

    spacer = widget.Spacer(
        background= custom_bg
    )
    
    return spacer

def get_spacer_flex(bg: str = "dark_gray") -> widget:
    custom_bg = NEW_COLORTHEME[bg]

    spacer = widget.Spacer(
        background= custom_bg,
        length = bar.STRETCH
    )
    
    return spacer


def icon(icon_name: str,bg: str = "light_gray", fg: str = "dark_gray") -> widget:
    selected_icon = ICONS.get(icon_name)
    custom_fg = NEW_COLORTHEME[fg]
    custom_bg = NEW_COLORTHEME[bg]

    return widget.TextBox(
            text= " " + selected_icon + " ",
            fontsize=14,
            padding=0,
            background= custom_bg,
            foreground=custom_fg,
    )
