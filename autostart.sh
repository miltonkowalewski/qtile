#!/bin/sh

nm-applet --indicator &
mkdir -p ~/wallpapers &
type -p feh >/dev/null || sudo apt install feh -y && cp -R /usr/share/backgrounds/* ~/wallpapers &
feh --randomize --bg-fill ~/wallpapers/* &
