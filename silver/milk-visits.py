# USACO 2019 December Contest, Silver
# Problem 3. Milk Visits
# https://usaco.org/index.php?page=viewproblem2&cpid=968

import sys

sys.stdin = open("milkvisits.in", "r")
sys.stdout = open("milkvisits.out", "w")

n,m = map(int,input().split())
farm = input()
road = [[] for i in range(n)]
for i in range(n-1):
	f1,f2 = map(int,input().split())
	road[f1-1].append(f2-1)
	road[f2-1].append(f1-1)
queris = []
for i in range(m):
	q = input().split()
	q[0], q[1] = int(q[0]) - 1, int(q[1]) - 1
	queris.append(q)
cow = [-1 for i in range(m)]
copnum = 0
for i in range(n):
	if cow[i] != -1:
		continue
	frontier = [i]
	currt = farm[i]
	while frontier:
		curr = frontier.pop()
		cow[curr] = copnum
		for n in road[curr]:
			if farm[n] == currt and cow[n] == -1:
				frontier.append(n)
	copnum +=1
final = ""
for a,b,milk in queris:
	if cow[a] == cow[b]:
		if farm[a] == milk:
			final += "1"
		else:
			final += "0"
	else:
		final += "1"

print(final)