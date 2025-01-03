# USACO 2017 January Contest, Silver
# Problem 2. Hoof, Paper, Scissors
# https://usaco.org/index.php?page=viewproblem2&cpid=691

import sys

sys.stdin = open("hps.in", "r")
sys.stdout = open("hps.out", "w")

n = int(input())
allval = []
games = []
for i in range(n):
    val = input()
    games.append(val)
pt = [0 for i in range(n)]
ht = [0 for i in range(n)]
st = [0 for i in range(n)]
for i in range(len(games)):
    if games[i] == "P":
        if i==0:
            st[i] +=1
        else:
            st[i] = st[i-1] +1
    else:
        if i == 0:
            st[i] = 0
        else:
            st[i] = st[i-1]

    if games[i] == "H":
        if i==0:
            pt[i] +=1
        else:
            pt[i] = pt[i-1] +1
    else:
        if i == 0:
            pt[i] = 0
        else:
            pt[i] = pt[i-1]

    if games[i] == "S":
        if i==0:
            ht[i] +=1
        else:
            ht[i] = ht[i-1] +1
    else:
        if i == 0:
            ht[i] = 0
        else:
            ht[i] = ht[i-1]

t = 0
val =0
for i in range(n): #p and h
    if (pt[i]) + (ht[len(ht)-1] - ht[i]) > val:
        val = (pt[i]) + (ht[len(ht)-1] - ht[i])

allval.append(val)
val =0
for i in range(n): #h and p
    if (ht[i]) + (pt[len(pt)-1] - pt[i]) > val:
        val = (ht[i]) + (pt[len(pt)-1] - pt[i])

allval.append(val)
val =0
for i in range(n): #p and s
    if (pt[i]) + (st[len(st)-1] - st[i]) > val:
        val = (pt[i]) + (st[len(st)-1] - st[i])

allval.append(val)
val =0
for i in range(n): #s and p
    if (st[i]) + (pt[len(pt)-1] - pt[i]) > val:
        val = (st[i]) + (pt[len(pt)-1] - pt[i])

allval.append(val)
val =0
for i in range(n): #s and h
    if (st[i]) + (ht[len(ht)-1] - ht[i]) > val:
        val = (st[i]) + (ht[len(ht)-1] - ht[i])

allval.append(val)
val =0
for i in range(n): #h and s
    if (ht[i]) + (st[len(st)-1] - st[i]) > val:
        val = (ht[i]) + (st[len(st)-1] - st[i])
        t = i
allval.append(val)
print(max(allval))