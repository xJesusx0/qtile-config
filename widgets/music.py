from libqtile.widget import base

from widgets.playerctl_config import *
from styles import NEW_COLORTHEME


class MusicMetadata(base.ThreadPoolText):
    
    defaults = [
        ("update_interval", 1, "polling rate in seconds"),
        ("background", NEW_COLORTHEME["light_gray"], ""),
        ("foreground", NEW_COLORTHEME["dark_gray"], ""),
        ("scroll_delay",5,""),
        ("scroll_interval",0.01,""),
        ("scroll_fixed_width", True, "Width of the widget in pixels"),  # Define un ancho fijo
        ("scroll", True, "Enable text scrolling if it exceeds the width"),

    ]

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, text='', **config)
        self.add_defaults(MusicMetadata.defaults)

    def get_metadata(self):
        x = PlayerCtl()
        result = x.get_current_metadata()
        return result

    def poll(self):
        metadata = self.get_metadata()
        # Actualiza el texto con la información deseada
        if metadata.title == "" and metadata.artist == "":
            return "Nothing is playing"
        
        return f"{metadata.title} - {metadata.artist}"