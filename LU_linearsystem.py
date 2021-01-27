import numpy as np

''' A.X = B
    LU.X = B
    U.X = L^(-1)B
    X = U^(-1).[L^(-1)B]'''
    
n = int(input('Type the dimension of the matrix: '))

a = np.zeros([n,n])
b = np.zeros([n,1])
Y = np.zeros([n,n])
U = np.zeros([n,n])
L = np.zeros([n,n])
X = np.zeros(n)

print('Type the elements of the matrix: ')

matrixA=[]
for i in range(n):
    line=[]
    for j in range(n):
        a[i][j] = float(input( 'a['+str(i+1)+']['+ str(j+1)+']='))
        aij=a[i][j]
        U[i,j]=a[i,j]
        line.append(aij)
    matrixA.append(line) 

print('\n Matrix A: ')
print('')
print(np.matrix(matrixA))  

# MATRIZ LU ---------------------------------------------------------

for k in range(n):
    for l in range (n):
        if (k==l):
            L[k,l]=1
        if (k<l):
            m=(a[l,k]/a[k,k])
            L[l,k]=m
            for c in range(n):
                a[l,c]=a[l,c]-(m*a[k,c])
                U[l,c]=a[l,c]               
                
print('\n Matrix L: ')
print('\n',L)
print('\n Matrix U: ')
print(U)
a=np.dot(L,U)
print('')
print('--- Checking if the decomposition is correct... ---')
print('')
print(a)
    
# MATRIZ B ---------------------------------------------------------

print('')
print('Digite os elementos da matriz B: ')
matrixB=[]
for i in range(n):
    lineb=[]
    for j in range(1):
        b[i][j] = float(input( 'a['+str(i+1)+']['+ str(j+1)+']='))
        bij=b[i][j]
        lineb.append(bij)
    matrixB.append(lineb)   
print('')
print('Matrix B:')
print('')
print(np.matrix(matrixB)) 

# Encontrando matrix X que é solução ------------------------------- 

invL = np.linalg.inv(L)
invU = np.linalg.inv(U)
Y = np.dot(invL,matrixB)
X = np.dot(invU,Y)
print('\n Final Matrix!!! :D ')
print('')
print(X)
