from dataclasses import dataclass, field

from colors.qtile_palette import QtilePalette


@dataclass
class GroupBoxStyle:
    
    palette: QtilePalette = field(default=QtilePalette())
    
    def stylize(self):
        return {
            "active": self.palette.active,
            "inactive": self.palette.inactive,
            "this_current_screen_border": self.palette.this_current_screen_border,
            "borderwidth": 2,
            "disable_drag": True,
            "font": 'Ubuntu Nerd Font',
            "fontsize": 14,
            "hide_unused": True,
            "highlight_method": 'line',
            "margin_x": 0,
            "margin_y": 4,
            "padding_x": 5,
            "padding_y": 8,
            "rounded": False,
            "urgent_alert_method": 'line'
        }

@dataclass
class BarStyle:

    palette: QtilePalette = field(default=QtilePalette())

    def stylize(self, **kwargs):
        return { **{
            "border_width": [2]*4,  # Draw top and bottom borders
            "border_color": [self.palette.this_current_screen_border]*4,
            "margin": [5,0,0,0],
        }, **kwargs }

@dataclass
class CurrentLayoutStyle:

    palette: QtilePalette = field(default=QtilePalette())
    
    def stylize(self):
        # "padding_x": 5,
        # "padding_y": 8,
        return {
            "font": 'Ubuntu Nerd Font',
            "fontsize": 10
        }
