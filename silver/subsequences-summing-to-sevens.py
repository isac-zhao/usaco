# USACO 2016 January Contest, Silver
# Problem 2. Subsequences Summing To Sevens
# https://usaco.org/index.php?page=viewproblem2&cpid=595

import sys

sys.stdin = open("div7.in", "r")
sys.stdout = open("div7.out", "w")
num = int(input())
possib = []
allinput = []

for n in range(num):
	a = int(input())
	allinput.append(a)

def psum(a):
	psum = [0]
	for i in a:
		psum.append(psum[-1] + i)
	return psum

prefix = psum(allinput)
remainders = []

for n in prefix:
	remainders.append(n % 7)

index = []
sizelis = []

for i in range(7):
	for n in range(len(remainders)):
		if remainders[n] ==i:
			index.append(n)

	if len(index) != 0:
		size = index[-1]-index[0]
		sizelis.append(size)

	index =[]		
print(max(sizelis))

