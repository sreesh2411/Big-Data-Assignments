#!/usr/bin/env python3
import sys

count = 0
prev_node = None
f=open(sys.argv[1],'w')
for inp in sys.stdin:
	inp=inp.strip()
	from_1,to_1 = inp.split('\t')
	if prev_node== from_1:
		adj_list.append(to_1)
	else:
		if prev_node:
			adj_list.sort()
			var=(",").join(adj_list)
			print('%s\t%s' % (prev_node,var))
			f.write('%s, %d\n' % (prev_node, 1))
		adj_list=[]
		adj_list.append(to_1)
		prev_node=from_1

if prev_node==from_1:
	adj_list.sort()
	var=(",").join(adj_list)
	print('%s\t%s' % (prev_node, var))
	f.write('%s, %d' % (prev_node, 1))
f.close()

