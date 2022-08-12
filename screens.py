from libqtile import bar
from libqtile.config import Screen
from libqtile.utils import guess_terminal

from colors.qtile_palette import QtilePalette, fallout_palette
from components import BarStyle
from widgets import *

qtile_palette = QtilePalette(**fallout_palette)
terminal = guess_terminal()

SCREEN_MODE = "w"
# SCREEN_MODE = "n"

if SCREEN_MODE == "w":
    fake_screens = [
        Screen( # SCREEN 1
            bottom=bar.Bar(
                [
                    w_layout,
                    w_group_box,
                    w_prompt,
                    w_window_name,
                    w_chord,
                    w_net,
                    w_net_graph,
                    w_memory,
                    w_memory_graph,
                    w_text_box(text="Cpu:"),
                    w_cpu_graph,
                    w_volume,
                    w_notify,
                    w_widget_box(widgets=[w_pomodoro,w_check_updates]),
                    w_systray,
                    w_clock,
                    w_quick_exit,
                ],
                24,
                **BarStyle(qtile_palette).stylize()
            ),
            x=0,
            y=0,
            width=1920*2,
            height=1080
        ),
    ]
else:
    fake_screens = [
        Screen( # SCREEN 1
            bottom=bar.Bar(
                [
                    w_layout,
                    w_group_box,
                    w_prompt,
                    w_window_name,
                    w_chord,
                    w_net,
                    w_net_graph,
                    w_memory,
                    w_memory_graph,
                    w_text_box(text="Cpu:"),
                    w_cpu_graph,
                    w_volume,
                    w_notify,
                    w_widget_box(widgets=[w_pomodoro,w_check_updates]),
                    w_systray,
                    w_clock,
                    w_quick_exit,
                ],
                24,
                **BarStyle(qtile_palette).stylize()
            ),
            x=0,
            y=0,
            width=1920,
            height=1080
        ),
        Screen( # SCREEN 2
            bottom=bar.Bar(
                [
                    w_layout,
                    w_group_box,
                    w_prompt,
                    w_window_name,
                    w_chord,
                    w_net,
                    w_net_graph,
                    w_memory,
                    w_memory_graph,
                    w_text_box(text="Cpu:"),
                    w_cpu_graph,
                    w_volume,
                    w_notify,
                    w_widget_box(widgets=[w_pomodoro,w_check_updates]),
                    w_systray,
                    w_clock,
                    w_quick_exit,
                ],
                24,
                **BarStyle(qtile_palette).stylize()
            ),
            x=1920,
            y=0,
            width=1920,
            height=1080
        ),
    ]
