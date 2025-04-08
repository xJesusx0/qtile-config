from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.config import Click, Drag, Key
from libqtile.widget import backlight

# custom imports de jesusxd
from global_vars import mod,TERMINAL

terminal = TERMINAL

MOUSE_BINDINGS = [
    # Drag floating layouts.
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

CUSTOM_KEYS = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "o", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    #Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
  
    # custom 
    Key([mod, "shift"], "h", lazy.hide_show_bar("bottom"), desc="ocultar / mostrar dock"),
    Key([mod, "shift"], "n", lazy.hide_show_bar("right"), desc="ocultar / mostrar panel lateral"),
    Key([mod, "shift"], "q", lazy.spawn("dunstctl close-all"), desc = "cerrar notificaciones"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="rofi, menu de aplicaciones"),
    Key([mod], "Print", lazy.spawn("flameshot gui"), desc="Take a screenshot with Flameshot"),

    Key([mod, "shift"], "v", lazy.spawn("code"), desc="vs code"),
    Key([mod, "shift"], "b", lazy.spawn("brave-browser"), desc="brave"),
    Key([mod], "Tab", lazy.spawn("rofi -show window"), desc="ventanas"),
    Key([mod], "p", lazy.spawn("/home/jesus/.config/polybar/cuts/scripts/powermenu.sh"), desc="powermenu"),

    Key([mod], "f6", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="mute"),
    Key([mod], "f7", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="bajar el volumen"),
    Key([mod], "f8", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="subir el volumen"),
    Key([mod], "f9", lazy.spawn("playerctl previous"), desc="prev song"),
    Key([mod], "f10", lazy.spawn("playerctl play-pause"), desc="play / pause"),
    Key([mod], "f11", lazy.spawn("playerctl next"), desc="next song"),
    Key([mod], "f2",  lazy.spawn("brightnessctl set 5%-"), desc="Bajar brillo"),
    Key([mod], "f3",  lazy.spawn("brightnessctl set +5%"), desc="Subir brillo"),
]
