import math
import numpy as np
k = np.zeros((10, 10))
x= np.zeros(10)
y= np.zeros(10)
n=int(input('Enter the number of data sets'))
print('Insert x variables')
for i in range(0,n,1):
    x[i]=int(input())
print('Insert y variables')
for i in range(0,n,1):
    y[i]=int(input())

for i in range(0,n,1):
    k[0][i]=y[i]

c=n-1
for i in range(1,n,1):
    for j in range(0,c,1):
        k[i][j]=k[i-1][j+1]-k[i-1][j]
    c=c-1

for i in range(0,n,1):
        print(k[i][0])


res=y[0]
g=21; # change x here
for i in range (1,n+1,1):
    p_prod=1
    h=int(x[i]-x[i-1])
    p=(g-x[0])/h
    for j in range (i,0,-1):
        D=p-j+1
        p_prod=p_prod*D
    res=res+(p_prod*k[0][i]/math.factorial(i))
print(res)
