from math import *
import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    if x>0:
        return cos(x)
    else:
        return sin(x)


#поиск порождающего вектора для матрицы Хаусхолдера
def Vect(x):
    if len(x)>1:
        norm=0
        e = np.array([[0]for i in range(len(x))])
        e[0][0]=1
        
        for i in range(len(x)):
            norm+=x[i]**2
        norm=sqrt(norm)

        if np.linalg.norm(x+norm*e)>=np.linalg.norm(x-norm*e):
            u=x+norm*e
        else:
            u=x-norm*e
            
        norm=0
        for i in range(len(x)):
            norm+=u[i]**2
        return u/sqrt(norm)
    
    else: return np.array([1])
#построение матрицы Хаусхолдера
def Hmatr(u):
    I=np.eye(n)
    h=np.eye(len(u))-2*u.dot(u.transpose())
    for i in range(len(h)):
        for j in range(len(h)):
            I[n-len(h)+i:][0][n-len(h)+j]=h[i][j]
    return I

#коэффициенты g_i(x)
def G(k,x):
    g=[]
    for j in range(k+1):
        if j>1:
            g.append((x*(2*(j-1)+1)*g[j-1] - (j-1)*g[j-2])/j)
        else:
            g.append((x**j))
    return g[k]   


n=int(input("Степень полинома "))+1 #тоже нет, это степень полинома 
m=int(input("Колличество интервалов "))+1 #нет, количество узлов = m+1
a=-1
b=1
#при M=8:
#x=[-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0]
#N=0, 1, 2, 5, 7, 8
x=[]
y=[]
for i in range(m):
    x.append(a+i*(b-a)/(m-1))# -1=x_0<...<x_m=-1 разбиение равномерное 
    y.append(fun(x[i]))


    

#построенние матрицы правой части
el=[[0.0 for i in range(n)] for i in range(n)]
el=np.array(el)
matr=np.copy(el)

for s in range(m):
    for j in range(n):
        for i in range(n):
            el[j][i]=G(j,x[s])*G(i,x[s])
    matr+=el

#матрица левой части
b=[[0] for i in range(n)]
for i in range(n):
    for s in range(m):
        b[i][0]+=y[s]*G(i,x[s])
b=np.array(b)

#сведение к системе {QAx=Q^T*b}
for k in range(n):
    bar=[]
    for j in range(n):
        if j>=k:
            bar.append([matr[j][k]])
    H=Hmatr(Vect(np.array(bar)))
    matr=H.dot(matr)
    b=H.transpose().dot(b)

#Поиск коэффициентов A_i - решение системы 
A=[0 for i in range(n)]
i=n-1
while i>=0:
    for j in range(n-i-1):
        A[i]-=A[i+j+1]*matr[i][i+j+1]
    A[i]=(A[i]+b[i])/matr[i][i]
    i-=1
A=np.array(A)

#построение графика функции Sum(A_i*g_i(x))
xp = []
gr = []

for i in range(1001):
    xp.append(x[0] + i*(x[m-1]-x[0])/1000)
    gr.append(0)
    for j in range(n):
        gr[i]+=(A[j]*G(j,xp[i]))

plt.scatter(x,y)
plt.plot(xp,gr)
plt.show()


