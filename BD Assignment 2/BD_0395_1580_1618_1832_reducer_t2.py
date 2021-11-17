#!/usr/bin/python3
import sys

#Initializing variables.
currentnode = None
count = 0
node = None
cumulative=0
for line in sys.stdin:
	
	line = line.strip()
	node, page_Rank = line.split('\t')
	try:
		page_Rank = float(page_Rank)     #Converting page_Rank into float type
	except ValueError:
		continue
	if (currentnode == node):
		cumulative += page_Rank         #Summing up all the page ranks.
	else:
		if currentnode:
			new_pagerank = 0.15+(0.85*cumulative)
			new_pr=round(new_pagerank,5)
			print('%s, %1.5f' % (currentnode, new_pr))
		cumulative = page_Rank
		currentnode = node
if (currentnode == node):
	new_pagerank = 0.15+(0.85*cumulative)
	new_pr=round(new_pagerank,5)
	print('%s, %1.5f' % (currentnode, new_pr))
