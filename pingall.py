#!/usr/bin/python
#
# python test script that pings all machines listed in a script
# Srivats Iyer, Cumulus Networks, 7/5/2016
#

import sys
import os


print " "
print "Pinging all machines listed in ping list..."
print " "

try:
   #open file stream
   inputfile = open('pinglist', 'r')
except IOError:
   print "There was an error reading file"
   sys.exit()

#print inputfile.read()

for line in inputfile:
	#  Chomp off carriage return on the end of the system name
	line = line[:-1]
	if os.system("ping -c 1 %s > /dev/null" %line) == 0:
		print "Host %s is UP!!!" %line		
        else:
		print "Host %s appears to be down!" %line


inputfile.close()
