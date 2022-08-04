# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from colors.qtile_palette import QtilePalette, default_palette, fallout_palette
from components import BarStyle, CurrentLayoutStyle, GroupBoxStyle

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    ### The essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Key([mod], "space", lazy.spawncmd(), desc="Spawn a command using a prompt widget"), ### Original
    Key([mod], "space", lazy.spawn("rofi -show run"), desc="Spawn a command using a prompt widget"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "r", lazy.restart()),

    ### Switch focus to specific monitor (out of three)
    Key([mod], "w", lazy.to_screen(0), desc='Keyboard focus to monitor 1'),
    Key([mod], "e", lazy.to_screen(1), desc='Keyboard focus to monitor 2'),

    ### Window controls
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), lazy.layout.section_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), lazy.layout.section_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    #Monad
    Key([mod], "g", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),

    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    ### Stack controls
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

]

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys.extend([
    Key([mod,"control"],"Right",  lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"control"],"Left", lazy.function(window_to_previous_screen, switch_screen=True)),
])

if os.path.isdir("hidden_modules"):
    from hidden_modules.keybinds import keybinds
    keys.extend(keybinds(mod))

groups = [Group(i) for i in "123456789"]

def focused_window(qtile, group_name):
    group = qtile.groups_map.get(group_name)
    group.cmd_toscreen()

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.function(focused_window, group_name=i.name),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + letter of group = switch focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
            # mod1 + shift + letter ofi.name group = switch to & move focused window to group
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            )
        ]
    )

# qtile_palette = QtilePalette(**default_palette)    
qtile_palette = QtilePalette(**fallout_palette)

layouts = [
    layout.MonadTall(
        border_focus=qtile_palette.active, # "Border colour(s) for the focused window.",
        border_normal="#000000", # "Border colour(s) for un-focused windows.",
        border_width=2, # "Border width.",
        single_border_width=None, # "Border width for single window",
        single_margin=None, # "Margin size for single window",
        margin=0, # "Margin of the layout",
        ratio=0.5, # "The percent of the screen-space the master pane should occupy " "by default.",
        min_ratio=0.25, # "The percent of the screen-space the master pane should occupy " "at minimum.",
        max_ratio=0.75, # "The percent of the screen-space the master pane should occupy " "at maximum.",
        min_secondary_size=85, # "minimum size in pixel for a secondary pane window ",
        change_ratio=0.05, # "Resize ratio",
        change_size=20, # "Resize change in pixels",
        new_client_position="after_current",
            # "Place new windows: "
            # " after_current - after the active window."
            # " before_current - before the active window,"
            # " top - at the top of the stack,"
            # " bottom - at the bottom of the stack,",
    ),
    layout.TreeTab(
        font = "Ubuntu",
        fontsize = 10,
        sections = ["Default"],
        section_fontsize = 8,
        border_width = 2,
        # bg_color = qtile_palette.this_current_screen_border,
        active_bg = qtile_palette.active,
        # active_fg = "000000",
        inactive_bg = qtile_palette.inactive,
        # inactive_fg = ,
        padding_left = 0,
        padding_x = 0,
        padding_y = 5,
        section_top = 10,
        section_bottom = 20,
        level_shift = 8,
        vspace = 3,
        panel_width = 250

    ),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=5, margin=10),
    # layout.Max(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=5, margin=10),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.RatioTile(),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(**CurrentLayoutStyle(qtile_palette).stylize()),
                widget.GroupBox(**GroupBoxStyle(qtile_palette).stylize()),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Net(
                    interface = "wlx503eaaa122f1",
                    format = 'Net: {down} ↓↑ {up}',
                    foreground = qtile_palette.active,
                    padding = 5
                ),
                widget.Memory(
                    foreground = qtile_palette.active,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    fmt = 'Mem: {}',
                    padding = 5
                ),
                widget.Systray(),
                widget.Clock(format = "%A, %B %d - %H:%M "),
                widget.QuickExit(),
            ],
            24,
            **BarStyle(qtile_palette).stylize()
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
