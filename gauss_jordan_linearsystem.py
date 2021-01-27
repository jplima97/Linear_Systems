import numpy as np
import sys

# Program to solve linear systems A.X = B
n = int(input('Type the dimension of the matrix: '))

a = np.zeros((n,n+1))
x = np.zeros(n)
g = np.zeros((n,n+1))

sys.stdout = open("output_GaussJordan.txt", "w")
# Augmented matrix ---------------------------------------------------
print('Type the elements of the augmented matrix: ')
matrixAB=[]
for i in range(n):
    line=[]
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i+1)+']['+ str(j+1)+']='))
        aij=a[i][j]
        line.append(aij)
    matrixAB.append(line)
    
print('')
print('--- Typed Matrix! ---')
print(np.matrix(matrixAB))    

# Gauss-Jordan Method ------------------------------------------------
for i in range(n):
    if a[i][i] == 0.0:
        print('The pivot cannot be zero!')
    
    for j in range(n):
        linha1=[]
        if i != j:
            m = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - m * a[i][k]

GaussMatrix=[]
for i in range(n):
    GaussLine=[]
    for k in range(n+1):
        g[i][k]=a[i][k]/a[i][i]
        value=g[i][k]
        GaussLine.append(round(value,2))
    GaussMatrix.append(GaussLine)
     
print('')
print('--- Gauss-Jordan Matrix: ---')            
print(np.matrix(GaussMatrix))
# Solution -----------------------------------------------------------
FinalMatrix=[]
for i in range(n):
    x[i] = g[i][k]
    solution=x[i]
    FinalMatrix.append(round(solution,2))
print('')    
print('Final Matrix! :)')
print(np.matrix(FinalMatrix).T)
