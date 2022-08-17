from libqtile import bar
from libqtile.config import Screen
from libqtile.utils import guess_terminal

from colors.qtile_palette import QtilePalette, fallout_palette
from components import BarStyle
from widgets import *

qtile_palette = QtilePalette(**fallout_palette)
terminal = guess_terminal()

# SCREEN_MODE = "w"
SCREEN_MODE = "dm"
SCREEN_MODE = "dm2"
# SCREEN_MODE = "n"

one_screen = Screen( # SCREEN 1
    bottom=bar.Bar(
        [
            w_layout,
            w_group_box(),
            w_prompt,
            w_window_name(background="#00000000"),
            w_notify,
            w_net,
            w_net_graph,
            w_memory,
            w_memory_graph,
            w_text_box(text="Cpu:"),
            w_cpu_graph,
            w_volume,
            w_systray,
            w_clock,
            w_quick_exit,
        ],
        24,
        **{**BarStyle(qtile_palette).stylize(), **{"background": "#00000000"}}
    ),
    x=5,
    y=5,
    width=1910,
    height=1070
)

fake_screens = [one_screen]

if SCREEN_MODE == "w":
    fake_screens = [
        Screen( # SCREEN 1 e 2
            bottom=bar.Bar(
                [
                    w_layout,
                    w_group_box(),
                    w_prompt,
                    w_window_name(),
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
elif SCREEN_MODE == "dm":
    fake_screens = [
        one_screen,
        Screen( # SCREEN 2
            bottom=bar.Bar(
                [
                    w_layout,
                    w_group_box(),
                    w_prompt,
                    w_window_name(),
                    w_widget_box(widgets=[w_pomodoro,w_check_updates]),
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
elif SCREEN_MODE == "dm2":
    fake_screens = [
        Screen( # SCREEN 1
            bottom=bar.Bar(
                [
                    w_layout,
                    w_group_box(),
                    w_prompt,
                    w_window_name(background="#00000000"),
                    w_net,
                    w_net_graph,
                    w_memory,
                    w_memory_graph,
                    w_text_box(text="Cpu:"),
                    w_cpu_graph,
                    w_volume,
                    w_systray,
                    w_clock,
                    w_quick_exit,
                ],
                24,
                **{**BarStyle(qtile_palette).stylize(), **{"background": "#00000000"}}
            ),
            x=5,
            y=5,
            width=1910,
            height=1070
        ),
        Screen( # SCREEN 2,
            bottom=bar.Bar(
                [
                    w_layout,
                    w_group_box(),
                    w_window_name(background="#00000000"),
                    w_notify,
                    w_quick_exit,
                ],
                24,
                **{**BarStyle(qtile_palette).stylize(), **{"background": "#00000000"}}
            ),
            x=1925,
            y=5,
            width=1910,
            height=1070
        ),
    ]
