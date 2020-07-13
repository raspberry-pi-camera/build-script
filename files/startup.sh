#!/bin/bash

if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
    echo "SSH - not starting camera"
else
    /opt/raspindi/bin/camera
fi