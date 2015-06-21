#!/usr/bin/python
import pyqrcode
import sys

NLINES = 15
OUTPUT_NAME = ''
ERROR_CORRECTION_LVL = 'H'
FILE = ''

#don't want to expirement with dictionaries
for arg in range(len(sys.argv)):
	if '-s' in sys.argv[arg]:
		FILE = sys.argv[arg + 1]
	if '-d' in sys.argv[arg]:
		OUTPUT_NAME = sys.argv[arg + 1] + '/'
	if '-e' in sys.argv[arg]:
		ERROR_CORRECTION_LVL = sys.argv[arg + 1]
	if '-n' in sys.argv[arg]:
		NLINES = sys.argv[arg + 1]

if len(sys.argv) == 1:
	print "Usage: " + sys.argv[0] + " args\n-s SOURCE_FILE\n-n NUMBER_OF_LINES_TO_GET (default is 15)\n-d DIR_NAME\n-e ERROR_CORRECTION_LVL (L=7%, M=15%, Q=25%, H=30%)(default H)\nThis program cuts text into multiple qr code svg files\n"
	sys.exit()


f=open(FILE)
chunk = 1
i = 0
while f.closed == False:
	line = ''
	for fline in f:
		line += fline 
		i += 1
		if i > NLINES:
			i = 0
			break
	print  line
	
	out = pyqrcode.create(line, error=ERROR_CORRECTION_LVL)
	out.svg( OUTPUT_NAME + str(chunk) +'.svg', scale=8)
	chunk += 1
	if i > 0:
		f.close()

