from libqtile import layout

from colors.qtile_palette import QtilePalette, fallout_palette

qtile_palette = QtilePalette(**fallout_palette)

layouts = [
    layout.Max(
        border_focus_stack=qtile_palette.active,
        border_width=2,
        margin=10
    ),
    layout.MonadWide(
        align=0,
        border_focus=qtile_palette.active, # "Border colour(s) for the focused window.",
        border_normal="#000000", # "Border colour(s) for un-focused windows.",
        border_width=2, # "Border width.",
        change_ratio=0.05, # "Resize ratio",
        change_size=20, # "Resize change in pixels",
        margin=0, # "Margin of the layout",
        max_ratio=0.75, # "The percent of the screen-space the master pane should occupy " "at maximum.",
        min_ratio=0.25, # "The percent of the screen-space the master pane should occupy " "at minimum.",
        min_secondary_size=85, # "minimum size in pixel for a secondary pane window ",
        new_client_position="after_current",
            # Place new windows: 
            #     after_current - after the active window. 
            #     before_current - before the active window, 
            #     top - at the top of the stack, 
            #     bottom - at the bottom of the stack,
        ratio=0.70, # "The percent of the screen-space the master pane should occupy " "by default.",
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
    # layout.MonadThreeCol(
    #     align=layout.MonadTall._left,
    #     border_focus=qtile_palette.active, # "Border colour(s) for the focused window.",
    #     border_normal="#000000", # "Border colour(s) for un-focused windows.",
    #     border_width=2, # "Border width.",
    #     change_ratio=0.05, # "Resize ratio",
    #     change_size=20, # "Resize change in pixels",
    #     main_centered=False,
    #     margin=0, # "Margin of the layout",
    #     max_ratio=0.75, # "The percent of the screen-space the master pane should occupy " "at maximum.",
    #     min_ratio=0.25, # "The percent of the screen-space the master pane should occupy " "at minimum.",
    #     min_secondary_size=85, # "minimum size in pixel for a secondary pane window ",
    #     new_client_position="after_current",
    #         # Place new windows: 
    #         #     after_current - after the active window. 
    #         #     before_current - before the active window, 
    #         #     top - at the top of the stack, 
    #         #     bottom - at the bottom of the stack,
    #     ratio=0.5, # "The percent of the screen-space the master pane should occupy " "by default.",
    #     single_border_width=None, # "Border width for single window",
    #     single_margin=None, # "Margin size for single window",
    # ),
    # layout.TreeTab(
    #     active_bg=qtile_palette.active, # Background color of active tab
    #     active_fg='ffffff', # Foreground color of active tab
    #     bg_color='000000', # Background color of tabs
    #     border_width=2, # Width of the border
    #     font="Ubuntu", # Font
    #     fontshadow=None, # font shadow color, default is None (no shadow)
    #     fontsize=10, # Font pixel size.
    #     inactive_bg=qtile_palette.inactive, # Background color of inactive tab
    #     inactive_fg='ffffff', # Foreground color of inactive tab
    #     level_shift=8, # Shift for children tabs
    #     margin_left=6, # Left margin of tab panel
    #     margin_y=6, # Vertical margin of tab panel
    #     padding_left=6, # Left padding for tabs
    #     padding_x=6, # Left padding for tab label
    #     padding_y=2, # Top padding for tab label
    #     panel_width=250, # Width of the left panel
    #     place_right=False, # Place the tab panel on the right side
    #     previous_on_rm=False, # Focus previous window on close instead of first.
    #     section_bottom=6, # Bottom margin of section
    #     section_fg='ffffff', # Color of section label
    #     section_fontsize=8, # Font pixel size of section label
    #     section_left=4, # Left margin of section label
    #     section_padding=4, # Bottom of margin section label
    #     section_top=4, # Top margin of section label
    #     sections=['Default'], # Titles of section instances
    #     urgent_bg='ff0000', # Background color of urgent tab
    #     urgent_fg='ffffff', # Foreground color of urgent tab
    #     vspace=2, # Space between tabs
    # ),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=5, margin=10),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.RatioTile(),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
