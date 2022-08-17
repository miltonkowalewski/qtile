from libqtile import qtile, widget
from libqtile.utils import guess_terminal

from colors.qtile_palette import QtilePalette, fallout_palette
from components import CurrentLayoutStyle, GroupBoxStyle

terminal = guess_terminal()
qtile_palette = QtilePalette(**fallout_palette)

def w_widget_box(widgets: list):
    return widget.WidgetBox(widgets=widgets)

def w_text_box(**kwargs):
    return widget.TextBox(**kwargs)

def w_group_box(**kwargs):
    return widget.GroupBox(**{**GroupBoxStyle(qtile_palette).stylize(), **kwargs})

def w_agroup_box(**kwargs):
    return widget.AGroupBox(**kwargs)

def w_window_name(**kwargs):
    return widget.WindowName(**{**{"foreground": "70ff70"}, **kwargs})

w_layout = widget.CurrentLayout(**CurrentLayoutStyle(qtile_palette).stylize())
w_prompt = widget.Prompt()
w_chord = widget.Chord(
    chords_colors={
        "launch": ("#ff0000", "#ffffff"),
    },
    name_transform=lambda name: name.upper(),
)
w_net = widget.Net(
    interface = "wlx503eaaa122f1",
    format = 'Net: {down} ↓↑ {up}',
    foreground = qtile_palette.active,
    padding = 5
)
w_net_graph = widget.NetGraph(graph_color="70ff70", fill_color=qtile_palette.active, border_color=qtile_palette.active)
w_memory = widget.Memory(
    foreground = qtile_palette.active,
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
    fmt = 'Mem: {}',
    padding = 5
)
w_memory_graph = widget.MemoryGraph(graph_color="70ff70", fill_color=qtile_palette.active, border_color=qtile_palette.active)
w_cpu_graph = widget.CPUGraph(graph_color="70ff70", fill_color=qtile_palette.active, border_color=qtile_palette.active)
w_volume = widget.Volume(foreground = "70ff70", emoji=True)
w_notify = widget.Notify()
w_pomodoro = widget.Pomodoro()
w_check_updates = widget.CheckUpdates()
w_systray = widget.Systray()
w_clock = widget.Clock(format = "%A, %B %d, %Y - %H:%M ", foreground = "70ff70")
w_quick_exit = widget.QuickExit(foreground = "70ff70")
w_spacer = widget.Spacer()
