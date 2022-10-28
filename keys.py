import os

from libqtile.config import Group, Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()


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


def focused_window(qtile, group_name):
    group = qtile.groups_map.get(group_name)
    group.cmd_toscreen()


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod],
        "space",
        lazy.spawn("rofi -show run"),
        desc="Spawn a command using a prompt widget",
    ),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "r", lazy.restart()),
    # Switch focus to specific monitor (out of three)
    Key([mod], "w", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    Key([mod], "e", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    # Window controls
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window",
    ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key(
        [mod, "shift"],
        "Down",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move window down",
    ),
    Key(
        [mod, "shift"],
        "Up",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move window up",
    ),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"],
        "Right",
        lazy.function(window_to_next_screen, switch_screen=True),
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.function(window_to_previous_screen, switch_screen=True),
    ),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_maximize(), desc="Toggle maximize"),
    # Monad
    Key([mod], "g", lazy.layout.grow()),
    Key([mod], "h", lazy.layout.shrink()),
    # Float
    # Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    ### Stack controls
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
]

if os.path.isdir("hidden_modules"):
    from hidden_modules.keybinds import keybinds

    keys.extend(keybinds(mod))

groups = [
    Group(name="1", label="1[W]orkspace", spawn=None, persist=True, layout="max"),
    Group(name="2", label="2[C]omunicação", spawn=None, persist=True, layout="monadtall"),
    Group(name="3", label="3[D]atabase", spawn=None, persist=True, layout="max"),
    Group(name="4", label="4[A]", spawn=None, persist=True),
    Group(name="5", label="5[B]", spawn=None, persist=True),
    Group(name="6", label="6[C]", spawn=None, persist=True),
    Group(name="7", label="7[S]sh", spawn=None, persist=True, layout="monadtall"),
    Group(name="8", label="8[B]rave", spawn=None, persist=True, layout="monadtall"),
    Group(name="9", label="9[P]layground", spawn=None, persist=True, layout="monadwide"),
    Group(name="0", label="0[C]ode", spawn=None, persist=True, layout="monadwide"),
]

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
            ),
        ]
    )
