#!/usr/bin/python3
import sys

if(len(sys.argv)>1):
	v=sys.argv[1]
file = open(v, "r")  #Inputting the v file to the mapper.
pagerank = dict()
for line in file:
	node, pr = line.split(", ")

	try:
		node = int(node)    #Converting node to integer type.
	except:
		pass
	pagerank[node] = float(pr)   #Returning the float value as the key to the node.

for line in sys.stdin:
	
	line = line.strip()
	from_node, adjacent = line.split("\t")
	split_nodes = adjacent.strip("'").split(',')
	nodes = [int(ele) if ele.isdigit() else ele for ele in split_nodes]  #Returning integer id stored as string.
	length = len(nodes)
	try:
		from_node = int(from_node) #Converting type to int.
	except:
		pass
	print('%s\t%f' % (from_node,0.0))
	for word in nodes: 
		try:
			if word in pagerank:
				contribution = pagerank[from_node]/length           #Calculating the contribution.
				print ('%s\t%f' % (word, contribution))
		except:
			continue
