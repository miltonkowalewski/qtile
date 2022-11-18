#!/bin/sh

type -p nm-applet >/dev/null || nm-applet --indicator &
type blueman-applet >dev/null || blueman-applet &
mkdir -p ~/wallpapers &
type -p feh >/dev/null || sudo apt install feh -y && cp -R /usr/share/backgrounds/* ~/wallpapers &
feh --randomize --bg-fill ~/wallpapers/* &
