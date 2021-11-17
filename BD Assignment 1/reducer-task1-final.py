#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

lineCount = 1
for line in sys.stdin:
    line = line.strip()

    line_list = line.split('#', 1)
    #print(line_list)
    word = line_list[0]
    count = line_list[1]
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print ('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

if current_word == word:
    print ('%s\t%s' % (current_word, current_count))
