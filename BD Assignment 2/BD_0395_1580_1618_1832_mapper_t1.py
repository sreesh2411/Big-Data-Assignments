#!/usr/bin/env python3
import sys
for inp in sys.stdin:
	inp=inp.strip()
	if inp.startswith('#'):
		continue
	try:
		from_1,to_1 = inp.split('\t')
	except:
		continue
	print ('%s\t%s' % (from_1,to_1))
