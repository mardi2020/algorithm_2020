def bin(n, k): # 재귀적 방법 구현
    if k == 0 or n == k:
        return 1
    else :
        return bin(n-1, k-1) + bin(n-1, k)


def bin2(n, k): # 배열을 이용한 구현
    B = [[0] * (k+1) for _ in range(n+1)]
    
    for i in range(0, n+1):
        for j in range(0, min(i, k)+1):
            if j == 0 or j == i :
                B[i][j] = 1
            else :
                B[i][j] = B[i-1][j-1] + B[i-1][j]

    return B[n][k]

print(bin(10, 5), bin2(10, 5))

##############################
from utility import *

def allShortestPath(g, n):
    d = g
    p = [[0] * n for _ in range(n)]
    printMatrix(d)

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if d[i][k]+d[k][j] < d[i][j] :
                    p[i][j] = k+1
                    d[i][j] = d[i][k] + d[k][j]              
                    
    return d, p

def _path(p, q, r):
    if p[q][r] != 0 :
        _path(p, q, p[q][r]-1)
        print(f"v{p[q][r]}", end=" ")
        _path(p, p[q][r]-1, r)


def path(p, q, r):
    print("v%d"% q, end=" ")
    _path(p, q - 1, r - 1)
    print("v%d"% r, end=" ")


inf = 1000
g = [[0,1,inf, 1,5],
   [9,0,3,2,inf],
   [inf,inf,0,4,inf],
   [inf,inf,2,0,3],
   [3,inf,inf,inf,0]]


d, p = allShortestPath(g,5)
print()
printMatrix(d)
print()
printMatrix(p) 
                 
path(p, 5, 3)
