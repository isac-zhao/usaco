# USACO 2017 February Contest, Silver
# Problem 2. Why Did The Cow Cross The Road II
# https://usaco.org/index.php?page=viewproblem2&cpid=715

import sys

sys.stdin = open("maxcross.in", "r")
sys.stdout = open("maxcross.out", "w")

f,s,t = map(int,input().split())
possib = [0] * f
com = []
for n in range(t):
    num = int(input())
    possib[num-1] = 1

for n in range(len(possib)-s+1):
    if n == 0:
        com.append(sum(possib[n:n+s]))

    elif n+s == len(possib):
        com.append(com[-1]-possib[-s-1])

    else:
        com.append(com[-1]-possib[n-1]+possib[n+s-1])

print(min(com))

