#Colors 
from dataclasses import dataclass

@dataclass(frozen=True)
class QtilePalette:
    
    inactive: str = "#e5e9f0"
    active: str = "#b48ead"
    this_current_screen_border: str = "#95eb8b"

fallout_palette = {
    "inactive": "#073605",
    "active": "#199515",
    "this_current_screen_border": "#199515"
}