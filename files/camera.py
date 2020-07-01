#!/usr/bin/env python3

import RPi.GPIO as GPIO
import subprocess
import os
from pathlib import Path

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

gui = GPIO.input(17)

if not gui:
    env = os.environ
    env['LD_LIBRARY_PATH'] = "/opt/raspindi/usr/lib"
    subprocess.call('/opt/raspindi/bin/raspindi', env=env)
else:
    with open("/tmp/neopixel.state", "w") as file:
        file.write("F")
    subprocess.call(['/usr/bin/raspistill', '-fp', '-t', '0', '-w', '1920',  '-h', '1080'])