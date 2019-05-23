#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###### DEFINITIONS ######

import numpy as np
import matplotlib.pyplot as plt

A = np.array([(15.,3.3,2.8),
              (3.7,4.,1.3),
              (3.8,1.3,10.1)])
I = np.array([(1.,0.,0.),
              (0.,1.,0.),
              (0.,0.,1.)])
EPSILON = 0.0001

LMIN = 0
LMAX = 20
Nlam = 100
nlam = 2
hlamnew = 0.001
hlam= 0.2

lamAr = np.zeros(Nlam)
lambdas = np.zeros(3)

###### ITERATIVE ######

def jacobi(A, size = 3):
    M = np.zeros([3,3])
    for i in range(size):
        M[i,i] = A[i,i]
    return M

def gaussSeidel(A, size = 3):
    M = np.zeros([3,3])
    for i in range(size):
        for j in range(size):
            if i <= j:
                M[i,j] = A[i,j]
    return M

def SOR(A, size = 3, omega =  0.9):
    M = np.zeros([3,3])
    for i in range(size):
        for j in range(size):
            if i < j:
                M[i,j] = A[i,j]
    for i in range(size):
        M[i,i] = A[i,i]*omega
    return M

def iterative(A, f, method, maxIteration = 1000):
    M = method(A)
    x = np.array([1.,1.,1.])
    MInv = np.linalg.inv(M)
    for step in range(maxIteration):
        r = f - np.dot(A,x)
        delta = np.dot(MInv, r)
        x = x + delta
        if np.linalg.norm(np.dot(-A,x)) < EPSILON:
            #print("Solved in ", step, " iterations")
            break
        if step == maxIteration-1:
            #print("Iteration limit reached")
            break
    return x/np.linalg.norm(x), step

###### EIGENVALUES ######

zeroline = lambda x: x - x;
funDet = lambda x: np.linalg.det(A-x*I)
funApr = funDet(LMIN)
funDetArr = np.zeros(Nlam)
lamArr = np.zeros(Nlam)
for nlami in range(Nlam):
    lami = LMIN+hlam*nlami
    lamAr[nlami] = lami
    funA = funDet(lami)
    funDetArr[nlami] = funA
    lamArr[nlami] = lami
    if funA*funApr < 0:
        lam = lami - hlam/2
        for new in range(20):
            funA1 = funDet(lam)
            lam = lam+hlamnew
            funA2 = funDet(lam)
            dfunA=(funA2-funA1)/hlamnew
            lam = lam-hlamnew
            lam = lam-funA1/dfunA
        lambdas[nlam] = lam
        nlam=nlam-1
    funApr = funA

plt.plot(lamArr, funDetArr)
plt.plot(lamArr, zeroline(lamArr))
plt.scatter(lambdas, zeroline(lambdas), marker='+')
plt.scatter(np.linalg.eig(A)[0], zeroline(lambdas), marker='x')
plt.show()
print("Eigenvalues: ")
print(np.linalg.eig(A)[0])
print("Estimated eigenvalues: ")
print(lambdas)
print("\n")

###### EIGENVECTORS ######


f = np.zeros(3)
string = ['First','Second','Third']

for nlam in range(3):
    Alam = A - np.dot(lambdas[nlam], I)
    print(string[nlam], "eigenvector")
    print("Jacobi: ")
    vector, step = iterative(Alam, f, jacobi)
    print(vector,"Steps:", step)
    print("GaussSeidel: ")
    vector, step = iterative(Alam, f, gaussSeidel)
    print(vector,"Steps:", step)
    print("SOR: ")
    vector, step = iterative(Alam, f, SOR)
    print(vector,"Steps:", step)
    print("Built-in: ")
    print(-np.matrix.transpose(np.linalg.eig(A)[1])[nlam])
    print("\n")
print(np.linalg.eig(A)[1])
    
            