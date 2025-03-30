from libqtile import bar, layout, qtile, widget, extension

LAYOUTS = [

    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_width = 0,
        single_border_width = 0,
        max_ratio = 0.75,
        new_client_position = 'after_current',
        margin = 6,
        #border_focus = COLORTHEME["yellow"]
        ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]