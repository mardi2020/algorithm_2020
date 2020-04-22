# p.7 [실습과제] 빠른정렬
def quickSort(s, low, high):
    if high > low :
        pivotPoint = partition(s, low, high)
        quickSort(s, low, pivotPoint-1)
        quickSort(s, pivotPoint+1, high)


def partition(s, low, high):
    pivotItem = s[low]
    j = low
    for i in range(low, high+1):
        if s[i] < pivotItem :
            j+=1
            s[i], s[j] = s[j], s[i]
    s[low], s[j] = s[j], s[low]
    return j

s = [3, 5, 2, 9, 10, 14, 4, 8]
quickSort(s, 0, 7)
print(s)


# p. 29 [실습과제] 큰 정수 곱셈
import math

def prod2(a, b):
    n = max(len(str(a)), len(str(b)))
    if a == 0 or b == 0 :
        return 0
    elif n <= 2 :
        return a * b
    m = int(math.floor(float(n)/2))

    x, y = a // pow(10, m), int(a % pow(10, m))
    w, z = b // pow(10, m), int(b % pow(10, m))
    r = prod2(x + y, w + z)
    p = prod2(x, w)
    q = prod2(z, y)
    
    return int(p * pow(10, 2*m) + (r - p - q) * pow(10, m) + q)

    
#a = 1234567812345678
a = 12315468523
b = 2345678923456789
print(prod2(a,b))
print(a*b)
