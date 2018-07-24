#!/usr/bin/env python
from subprocess import Popen
import subprocess
import time
import re

def start():
    # Runs the command in another process. Doesn't block
    process = Popen(['nm-applet', ''],
        bufsize=1,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        shell=True)
    # Later
    # Returns the return code of the command. None if it hasn't finished
    while process.poll() is None: 
        print 'running'
        time.sleep(1)
        out = process.stdout.readline()
        
        regex = r"nm-applet-CRITICAL"
        matches = re.finditer(regex, out, re.MULTILINE)
        if matches:
            print 'stoping'
            Popen(['killall', 'nm-applet'])
            return
    print 'not runng'

while True:
    start()