import numpy as np
import sys

''' A.X = B
    LU.X = B
    U.X = L^(-1)B
    X = U^(-1).[L^(-1)B]'''
    
n = int(input('Digite a dimensão da matriz: '))

'''np.zero Retorna uma matriz com zeros. Como queremos a matriz 
   aumentada, ficamos com: (nome)=np.zeros(Dimensao)'''

a = np.zeros([n,n])
b = np.zeros([n,1])
Y = np.zeros([n,n])
U = np.zeros([n,n])
L = np.zeros([n,n])
X = np.zeros(n)

sys.stdout = open("output_LU.txt", "w")

print('Digite os elementos da matriz: ')
matrizA=[]
for i in range(n):
    linha=[]
    for j in range(n):
        a[i][j] = float(input( 'a['+str(i+1)+']['+ str(j+1)+']='))
        aij=a[i][j]
        U[i,j]=a[i,j]
        linha.append(aij)
    matrizA.append(linha) 

print('\n Matriz A: ')
print('')
print(np.matrix(matrizA))  

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
                
print('\n Matriz L: ')
print('\n',L)
print('\n Matriz U: ')
print(U)
a=np.dot(L,U)
print('')
print('--- Verificando se a decomposição está certa ---')
print('')
print(a)
    
# MATRIZ B ---------------------------------------------------------

print('')
print('Digite os elementos da matriz B: ')

matrizB=[]
for i in range(n):
    linhab=[]
    for j in range(1):
        b[i][j] = float(input( 'a['+str(i+1)+']['+ str(j+1)+']='))
        bij=b[i][j]
        linhab.append(bij)
    matrizB.append(linhab)   
print('')
print('Matriz B:')
print('')
print(np.matrix(matrizB)) 

# Encontrando matrix X que é solução ------------------------------- 

invL = np.linalg.inv(L)
invU = np.linalg.inv(U)
Y = np.dot(invL,matrizB)
X = np.dot(invU,Y)
print('\n Matriz solução!!! :D ')
print('')
print(X)
