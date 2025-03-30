from libqtile import widget

def get_current_layout() -> widget:
    return widget.CurrentLayout(
            fmt=' {}',
          #  foreground=colors[2],
           # background=colors[7],
            padding=5
        )
    