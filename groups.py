from libqtile.config import Group

custom_labels = {
    "1": "",   # Grupo 1
    "2": "󰄛",   # Grupo 2
    "3": "",   # Grupo 3
    "4": "",   # Grupo 4
    "5": "",   # Grupo 5
    "6": "",   # Grupo 6
    "7": "",   # Grupo 7
    "8": "",   # Grupo 8
    "9": "",   # Grupo 9
    "0": "",
}

GROUP_NAMES = "1234567890"

GROUPS = [Group(i,label=custom_labels[i]) for i in GROUP_NAMES]


