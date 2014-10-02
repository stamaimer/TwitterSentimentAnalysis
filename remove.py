import codecs
import sys

ifile = codecs.open(sys.argv[1], 'r', 'utf-8')
ofile = codecs.open(sys.argv[2], 'w', 'utf-8')

lines = ifile.readlines()

tmp = set()

for line in lines:

    tmp.add(line)

for line in tmp:

    if 'RT' not in line:

        ofile.write(line)

ifile.close()
ofile.close()

print "eof..."
