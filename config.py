from libqtile import layout, qtile
from libqtile.config import Click, Drag, Key, Match, Screen
from libqtile.lazy import lazy

from custom_keys import CUSTOM_KEYS, MOUSE_BINDINGS
from layouts import LAYOUTS
from groups import GROUPS
from bars import TOP_BAR, BOTTOM_BAR
from utils import add_groups_switch_bindings, add_waylands_switch_vt_bindings, load_initial_setup

keys = CUSTOM_KEYS
add_waylands_switch_vt_bindings(keys)

groups = GROUPS
add_groups_switch_bindings(keys,groups)

layouts = LAYOUTS

widget_defaults = dict(
    font="jetbrainsmono",
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top = TOP_BAR,
        bottom = BOTTOM_BAR
    ),
]

mouse = MOUSE_BINDINGS

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus="#d65d0e",  # Color del borde cuando la ventana está enfocada
    border_normal="#00000000",  # Color del borde cuando la ventana no está enfocada
    border_width=1,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        #Match(wm_class="crx_hnpfjngllnobngcgfapefoaidbinmjnm")
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

load_initial_setup()
