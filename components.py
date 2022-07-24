from dataclasses import dataclass, field
from colors.qtile_palette import QtilePalette

@dataclass
class GroupBox:
    
    palette: QtilePalette = field(default=QtilePalette())
    
    def run(self):
        return {
            "active": self.palette.active,
            "inactive": self.palette.inactive,
            "this_current_screen_border": self.palette.this_current_screen_border,
            "borderwidth": 2,
            "disable_drag": True,
            "font": 'Ubuntu Nerd Font',
            "fontsize": 14,
            "hide_unused": False,
            "highlight_method": 'line',
            "margin_x": 0,
            "margin_y": 3,
            "padding_x": 5,
            "padding_y": 8,
            "rounded": False,
            "urgent_alert_method": 'line'
        }
