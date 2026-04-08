

from easydict import EasyDict as edict

__C = edict()
cfg = __C

# print debug info
__C.MONITOR_TIME = 1
__C.DBG_PRT = 0

# web UI parameters:
__C.DL_obj_sel_en = 0

# Grabcut algorithm parameters
__C.GC_iter_count = 2

__C.FIXED_CLASSES = [
    {"name": "Vegetative - Low",  "color": "#5D8A3C"},  # olive green
    {"name": "Vegetative - High", "color": "#1A4A0A"},  # dark green
    {"name": "C&D - Low",         "color": "#C8A96E"},  # tan
    {"name": "C&D - High",        "color": "#7A3B1E"},  # dark brown
]
