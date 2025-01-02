# USACO 2018 January Contest, Silver
# Problem 3. MooTube
# https://usaco.org/index.php?page=viewproblem2&cpid=788#

import sys

sys.stdin = open("mootube.in", "r")
sys.stdout = open("mootube.out", "w")

n,q = map(int,input().split())
neighbor = [[] for i in range(n+1)]
for i in range(n-1):
	f1,f2,f3 = map(int,input().split())
	neighbor[f1-1].append((f2-1,f3))
	neighbor[f2-1].append((f1-1,f3))
def searchvids(vid,threshold):
	global numreach
	visited[vid] = True
	for n in neighbor[vid]:
		if not visited[n[0]] and n[1] >= threshold:
			numreach += 1
			searchvids(n[0],threshold)
visited = []
for i in range(q):
	threshold, start = map(int,input().split())
	start -=1
	numreach = 0
	visited = [False] * n
	searchvids(start,threshold)
	print(numreach)
