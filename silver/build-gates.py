# USACO 2016 January Contest, Silver
# Problem 3. Build Gates
# https://usaco.org/index.php?page=viewproblem2&cpid=596

import sys

sys.stdin = open("gates.in", "r")
sys.stdout = open("gates.out", "w")

n = int(input())
fence = input()
counter =0
visedge = set()
visnode = set()
prev = (0,0)
visnode.add(prev)
for d in fence:
	x,y = prev
	if d == "N":
		x+=1
	elif d == "S":
		x-=1
	elif d == "E":
		y-=1
	elif d == "W":
		y+=1
	if ((x, y), prev) not in visedge and (x, y) in visnode:
		counter += 1
	visedge.add(((x, y), prev))
	visedge.add((prev, (x, y)))
	visnode.add((x, y))

	prev = (x, y)
print(counter)