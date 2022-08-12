from libqtile import layout

from colors.qtile_palette import QtilePalette, fallout_palette

qtile_palette = QtilePalette(**fallout_palette)

layouts = [
    layout.MonadThreeCol(
        align=layout.MonadTall._left,
        border_focus=qtile_palette.active, # "Border colour(s) for the focused window.",
        border_normal="#000000", # "Border colour(s) for un-focused windows.",
        border_width=2, # "Border width.",
        change_ratio=0.05, # "Resize ratio",
        change_size=20, # "Resize change in pixels",
        main_centered=False,
        margin=5, # "Margin of the layout",
        max_ratio=0.75, # "The percent of the screen-space the master pane should occupy " "at maximum.",
        min_ratio=0.25, # "The percent of the screen-space the master pane should occupy " "at minimum.",
        min_secondary_size=85, # "minimum size in pixel for a secondary pane window ",
        new_client_position="after_current",
            # Place new windows: 
            #     after_current - after the active window. 
            #     before_current - before the active window, 
            #     top - at the top of the stack, 
            #     bottom - at the bottom of the stack,
        ratio=0.5, # "The percent of the screen-space the master pane should occupy " "by default.",
        single_border_width=None, # "Border width for single window",
        single_margin=None, # "Margin size for single window",
    ),
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
