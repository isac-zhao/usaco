# USACO 2017 Febuary Contest, Silver
# Problem 3. Why Did the Cow Cross the Road III
# https://usaco.org/index.php?page=viewproblem2&cpid=716

import sys

sys.stdin = open("countcross.in", "r")
sys.stdout = open("countcross.out", "w")

n,k,r = map(int,input().split())
fence = set()
for i in range(r):
	x,y,a,b = map(int,input().split())
	fence.add(((x-1,y-1),(a-1,b-1)))
	fence.add(((a-1,b-1),(x-1,y-1)))
cow = set()
for i in range(k):
	x,y = map(int,input().split())
	cow.add((x-1,y-1))
count = 0
def isblocked(p1,p2):
	return (p1,p2) in fence
def floodfill(x,y,n,cowset,visited):
	count = 0
	tovisit = {(x,y)}
	while tovisit:
		cx,cy = tovisit.pop()
		if (cx,cy) not in visited:
			visited.add((cx,cy))
			for nx,ny in ((cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1)):
				if 0 <= nx < n and 0 <= ny < n and not isblocked((cx,cy),(nx,ny)):
					tovisit.add((nx,ny))
			if (cx,cy) in cowset:
			    count += 1
				
	return count

total = sum(range(k))
cowset = set(cow)
visited = set()
for c in cow:
    if c not in visited:
        cowcount = floodfill(c[0],c[1],n,cowset,visited)
        total -= (cowcount * (cowcount - 1)) // 2
print(total)


