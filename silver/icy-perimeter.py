# USACO 2019 January Contest, Silver
# Problem 2. Icy Perimeter
# https://usaco.org/index.php?page=viewproblem2&cpid=895
import sys

sys.stdin = open("perimeter.in", "r")
sys.stdout = open("perimeter.out", "w")

def floodfill(x,y):
    global visited
    tovisit = {(x,y)}
    area = 0
    perimeter = 0
    count = 0
    while tovisit:
        x,y = tovisit.pop()
        if (x,y) not in visited:
            count += 1
            visited.add((x,y))
            area+=1
            neighbor = 0
            for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0 <= nx < length and 0 <= ny < length and graph[nx][ny] == "#":
                    tovisit.add((nx,ny))
                    neighbor += 1
            perimeter += 4-neighbor
    return (area,perimeter)

length = int(input())

graph = []
for i in range(length):
    j = input()
    graph.append(j)
terminate = False
for row in graph:
    if row.count(".") !=0:
        break
else:
    print(length **2,length*4)
    terminate = True
if not terminate:
    visited = set()
    maxa = 0
    minp = 0
    for row in range(length):
        for col in range(length):
            if graph[row][col] == "#":
                area,perimeter = floodfill(row,col)
                if area > maxa or (area == maxa and perimeter < minp):
                    maxa =area
                    minp = perimeter
    print(maxa,minp)
