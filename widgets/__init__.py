
from libqtile import qtile
from libqtile import widget

# Local imports - widgets
from widgets.clock import clock_widget, date_widget
from widgets.general_widgets import *
from widgets.music import MusicMetadata
from widgets.separators import *
from widgets.system_widgets import *

TOP_BAR_WIDGETS =  [
    ### left modules
    # main icon
    get_separator("yellow"),
    system_image,
    get_right_arrow(),

    # group box
    get_separator(),
    groupbox_widget,
    get_right_arrow("blue","dark_gray"),

    # disk usage
    get_separator("blue"),
    icon("disk","blue", "light_gray"),
    disk_widget,
    get_right_arrow("yellow", "blue"),
    
    #network
    get_separator("yellow"),
    icon("wlan", "yellow", "dark_gray"),
    wlan_widget,
    get_right_arrow("dark_gray", "yellow"),

    # spacer
    get_spacer(),

    ### right modules

    #systray_widget,
    get_separator(),
    get_left_arrow("dark_gray", "blue"),
    icon("temperature","blue","light_gray"),
    thermal_sensor_widget, 
    get_separator("blue"),

    # memory
    get_left_arrow("blue","light_gray"),
    icon("memory"),
    get_separator("light_gray"),
    memory_widget,
    get_separator("light_gray"),

    # volume
    get_left_arrow("light_gray", "red"),
    icon("volume","red","dark_gray"),
    volume_widget,
    get_separator("red"),

    # calendar
    #get_left_arrow("blue", "red"),
    #icon("calendar","red"),
    #date_widget,
    #get_separator("red"),

    # clock
    get_left_arrow("red", "dark_gray"),
    icon("clock","dark_gray","light_gray"),
    clock_widget,
    get_separator("dark_gray"),

    # batery
    get_left_arrow("dark_gray","yellow"),
    icon("battery","yellow"),
    battery_widget,
    get_separator("yellow")
]

BOTTOM_BAR_WIDGETS = [

    get_separator("light_gray"),
    icon("music", "light_gray", "dark_gray"),
    MusicMetadata(width = 250,),
    get_right_arrow("dark_brown", "light_gray"),

    get_separator("dark_brown"),
    previous_song,

    get_separator("dark_brown"),
    play_pause,

    get_separator("dark_brown"),
    next_song,
    get_right_arrow("blue","dark_brown"),

    icon("clipboard", "blue", "light_gray"),
    clipboard_widget,
    get_right_arrow("dark_gray","blue"),

    get_spacer(),
    tasklist_widget,
    
    #get_left_arrow("medium_gray","dark_gray"),
    status_notifier_widget,
    bluetooth_widget,    

    get_left_arrow("medium_gray","red"),
    icon("cpu", "red", "dark_gray"), 
    cpu_widget,
    get_separator("red"),

    get_left_arrow("red","yellow"),
    icon("brightness", "yellow"),
    brightness_widget,
    get_separator("yellow"),

    # us_fr_image,
]
