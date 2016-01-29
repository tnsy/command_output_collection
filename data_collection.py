#!/usr/bin/env python

import os
import time
from sys import argv, stdout

script, filename = argv

commands_to_run = []
border = '\n+++++++++++++++++++++++++++\n\n'
border1 = '\n<><><><><><><><><><><><><><><><>\n\n'

number_of_commands = int(raw_input('How many commands do you want to run\n> '))

for i in range(0,number_of_commands):
    i = i + 1
    commandc = raw_input('\nInput command %s:\n> ' % i)
    commands_to_run.append(commandc)

x = int(raw_input('\nHow many times do you want this to be collected?\n> '))
time_interval = int(raw_input('\nInterval in seconds\n> '))
time_to_complete = (x * time_interval - time_interval)
print '\n\nThis will take %s minutes and %s seconds to complete\n\n' % (time_to_complete / 60, time_to_complete % 60)

file = open(filename, 'w')
file.write('Below file is an output of commands: %r\n' % commands_to_run)
file.write(border)

for i in range(0,x):
    run = i + 1
    current_time = time.ctime()
    universal_time = str(time.time())
    file.write('\tRun: %s' % run)
    file.write('\n\nCollected at: %s' % current_time)
    file.write('\nEpoch time: %s\n\n' % universal_time)
    for cmd in commands_to_run:
	c = os.popen('%s' % cmd)
	command = c.read()
	file.write(command)
	file.write(border1)
    stdout.write('\rRunning %s out of %s' % (run, x))
    stdout.flush()
    if i < (x - 1):
        time.sleep(time_interval)
	file.write(border)

print '\n\nOutput collected to %s > exiting' % filename
file.close()
