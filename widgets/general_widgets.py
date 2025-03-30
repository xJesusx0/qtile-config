from libqtile import widget, qtile

from styles import NEW_COLORTHEME

system_image = widget.Image(
    #filename="~/.config/qtile/icons/fedora.png",
    #filename="/home/jesus/Imágenes/icon.jpg",
    filename="/home/jesus/Imágenes/ubuntu3.png",
    scale="True",
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("/home/jesus/.config/polybar/cuts/scripts/powermenu.sh")},
    background=NEW_COLORTHEME["yellow"],
    margin=4
)

us_fr_image = widget.Image(
    #filename="~/.config/qtile/icons/fedora.png",
    # filename="/home/jesus/Imágenes/icon.jpg",
    filename="/home/jesus/Descargas/IMG-20250201-WA0021.jpg",
    scale="True",
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("/home/jesus/.config/polybar/cuts/scripts/powermenu.sh")},
    background=NEW_COLORTHEME["dark_gray"],
    margin=0
)
