from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy

import os
from global_vars import mod

def add_waylands_switch_vt_bindings(keys: list) -> None:

    # Add key bindings to switch VTs in Wayland.
    # We can't check qtile.core.name in default config as it is loaded before qtile is started
    # We therefore defer the check until the key binding is run by using .when(func=...)
    for vt in range(1, 8):
        keys.append(
            Key(
                ["control", "mod1"],
                f"f{vt}",
                lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
                desc=f"Switch to VT{vt}",
            )
        )

def add_groups_switch_bindings(keys: list, groups: list) -> None:
    for i in groups:
        keys.extend(
            [
                # mod + group number = switch to group
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc=f"Switch to group {i.name}",
                ),
                # mod + shift + group number = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc=f"Switch to & move focused window to group {i.name}",
                ),
                # Or, use below if you prefer not to switch to that group.
                # # mod + shift + group number = move focused window to group
                # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                #     desc="move focused window to group {}".format(i.name)),
            ]
        )

def load_initial_setup() -> None:

    # Apps al inicio
    autostart = [
            "feh --bg-fill /home/jesus/Descargas/gruvbox_girl.png",
            "picom --config /home/jesus/.config/picom/config.conf &"
        ]

    for x in autostart:
        os.system(x)


def parse_text(text:str) -> str:
    print('<<<<<<<<<<<<<<<',text)
    splitted = text.split('-')
    return splitted[0]

