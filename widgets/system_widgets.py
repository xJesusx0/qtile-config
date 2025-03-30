from libqtile import widget,qtile
from xdg import BaseDirectory

from styles import NEW_COLORTHEME, ICONS
from utils import parse_text
from widgets.decorations import decoration

memory_widget = widget.Memory(
    foreground= NEW_COLORTHEME["dark_gray"],
    background=NEW_COLORTHEME["light_gray"],
    fmt='{}Mb',
    format='{MemUsed:.0f}',
    padding=0,
    decorations = decoration
)

disk_widget = widget.DF(
    fmt="{}",
    foreground= NEW_COLORTHEME["light_gray"],
    background=NEW_COLORTHEME["blue"],
    format="{uf}{m}",
    visible_on_warn=False,
    partition="/",
    padding=5    
)

battery_widget = widget.Battery(
    foreground = NEW_COLORTHEME["dark_gray"],
    background = NEW_COLORTHEME["yellow"],
    format = '{percent:2.0%} {char}',
    full_short_text = '100% ',
    discharge_char = '󰁅',
    charge_char='󱐋',
    full_char = '',
    update_interval=2
)

volume_widget = widget.PulseVolume(
    background = NEW_COLORTHEME["red"],
    foreground = NEW_COLORTHEME["dark_gray"]
)

groupbox_widget = widget.GroupBox(
    font="JetBrainsMono Nerd Font Mono",
    fontsize=24,
    spacing=1,
    border_width=20,
    rounded=False,
    disable_drag=True,
    highlight_method="block",
    active=NEW_COLORTHEME["blue"],
    inactive=NEW_COLORTHEME["light_gray"],
    highlight_color=NEW_COLORTHEME["medium_gray"],
    this_current_screen_border=NEW_COLORTHEME["medium_gray"], # line color
    block_highlight_text_color=NEW_COLORTHEME["red"], # icon color
    #this_screen_border=NEW_COLORTHEME["green"],
    #other_current_screen_border=NEW_COLORTHEME["red"],
    #other_screen_border=NEW_COLORTHEME["red"],
    foreground=NEW_COLORTHEME["red"],
    background=NEW_COLORTHEME["dark_gray"]
)

wlan_widget = widget.Wlan(
    font="JetBrainsMono Nerd Font",
    #padding=0,
    fontsize=13,
    #fmt='<b>{}</b>',
    foreground = NEW_COLORTHEME["dark_gray"],
    background = NEW_COLORTHEME["yellow"],
    interface = "wlo1",
    format='{essid} {percent:2.0%}',
    disconnected_message = "disconnected"
)

systray_widget = widget.Systray(
    background=NEW_COLORTHEME["medium_gray"],
    padding=5
)

status_notifier_widget = widget.StatusNotifier(
    background=NEW_COLORTHEME["medium_gray"],
    padding=5
) 

windowname_widget = widget.WindowName(
    foreground=NEW_COLORTHEME["light_gray"],
    background=NEW_COLORTHEME["blue"],
    format='{name}',
    empty_group_string = '<3',
    scroll_fixed_width= False,
    max_chars=200,
    width=300,
    scroll_clear = True,
    scroll= True
)

tasklist_widget = widget.TaskList(
    background = NEW_COLORTHEME["medium_gray"],
    border = NEW_COLORTHEME['dark_gray'],
    margin = 4,
    rounded = True,
    highlight_method = 'block',
    padding = 4,
    icon_size = 14,
    txt_floating = '  ',
    txt_maximized = ' ',
    txt_minimized = '  ',
    #parse_text = parse_text,
    max_title_width = 150
)

thermal_sensor_widget = widget.ThermalSensor(
    background = NEW_COLORTHEME["blue"],
    foreground = NEW_COLORTHEME["light_gray"],
    padding=5

)

brightness_widget = widget.Backlight(
    backlight_name = 'amdgpu_bl0',
    background = NEW_COLORTHEME["yellow"],
    foreground = NEW_COLORTHEME["dark_gray"],
    border = 10,
) 


cpu_widget = widget.CPU(
    background = NEW_COLORTHEME["red"],
    foreground =NEW_COLORTHEME["dark_gray"],
    format = '{freq_current}GHz',
    scroll = True,
    width = 100
)

bluetooth_widget = widget.Bluetooth(
    background = NEW_COLORTHEME["blue"],
    foreground =NEW_COLORTHEME["light_gray"],
    default_show_battery = True,
    margin = 5,
    default_text = '{connected_devices}'
)

previous_song = widget.TextBox(
    fontsize = 18,
    text= ICONS["previous"],
    background= NEW_COLORTHEME["dark_brown"],
    foreground= NEW_COLORTHEME["light_gray"],
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("playerctl previous")},
)


next_song = widget.TextBox(
    fontsize = 18,
    text= ICONS["next"],
    background= NEW_COLORTHEME["dark_brown"],
    foreground= NEW_COLORTHEME["light_gray"],
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("playerctl next")},
)

play_pause = widget.TextBox(
    fontsize = 18,
    text= ICONS["play_pause"],
    background= NEW_COLORTHEME["dark_brown"],
    foreground= NEW_COLORTHEME["light_gray"],
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("playerctl play-pause")},
)

clipboard_widget = widget.Clipboard(
    background= NEW_COLORTHEME["blue"],
    foreground= NEW_COLORTHEME["light_gray"],
    width = 200,
    max_width = 200,
    #max_chars = 200,
    #scroll_fixed_width = True,
    scroll = True,
    timeout = 30,
    scroll_delay = 5,
    scroll_interval = 0.01
)