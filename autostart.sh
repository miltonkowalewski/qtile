#!/bin/sh
/bin/bash ~/.config/qtile/notification.sh /var/log/notification/log.txt &
nm-applet &
feh --bg-scale ~/.config/qtile/background.jpg &