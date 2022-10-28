#Colors 
from dataclasses import dataclass


@dataclass(frozen=True)
class QtilePalette:
    
    inactive: str = "#e5e9f0"
    active: str = "#b48ead"
    this_current_screen_border: str = "#95eb8b"

fallout_palette = {
    "inactive": "#073605",
    "active": "#0fff08",
    "this_current_screen_border": "#199515"
}

default_palette = {
    "inactive": "#e5e9f0",
    "active": "#b48ead",
    "this_current_screen_border": "#95eb8b"
}
