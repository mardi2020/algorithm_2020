
# p.11 matrix chain multiplication
import utility

def order(p,i,j):
    # 구현
    if i == j:
        print(f"A{i} ", end="")
    else:
        k = p[i][j]
        print("(", end="")
        order(p, i, k)
        order(p, k+1, j)
        print(")", end="")
  #   
  
d=[5,2,3,4,6,7,8]
n=len(d)-1

m=[[0 for j in range(1,n+2)] for i in range(1,n+2)]
p=[[0 for j in range(1,n+2)] for i in range(1,n+2)]


# 구현
for diagonal in range(1, n): # 1 ~ 5
    for i in range(1, n-diagonal+1): 
        j = i + diagonal
        
        min_value = 9999
        for k in range(i, j): 
            x = m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
            if min_value > x :
                min_value, m[i][j] = x, x 
                p[i][j] = k                 
#

utility.printMatrix(m)
print()
utility.printMatrix(p)
order(p,1,6)


print('\n\n')
# p.23 Optimal Binary Search Tree

class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data = data

def tree(key,r,i,j):
    k=r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
        return p

key=[" ","A","B","C","D"]
p=[0,0.375, 0.375, 0.125,0.125]
n=len(p)-1

a=[[0 for j in range(0,n+2)] for i in range(0,n+2)]
r=[[0 for j in range(0,n+2)] for i in range(0,n+2)]

for i in range (1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0

#구현
for diagonal in range(1, n):
    for i in range(1, n-diagonal+1):
        j = i + diagonal

        min_value = 9999
        for k in range(i, j+1): # sum of i~j 
            Sum_p = 0
            for u in range(i, j+1):
                Sum_p += p[u]

            x = a[i][k-1] + a[k+1][j] + Sum_p
            if min_value > x: # minimum
                min_value, a[i][j] = x, x
                r[i][j] = k
#

utility.printMatrixF(a)
print()
utility.printMatrix(r)

root=tree(key,r,1,n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)
