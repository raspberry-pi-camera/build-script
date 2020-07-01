#!/bin/bash

if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
    echo "SSH - not starting camera"
else
    touch /run/user/1000/neopixel.state

    sudo /opt/raspindi/bin/neopixel &
    /opt/raspindi/bin/camera
fi