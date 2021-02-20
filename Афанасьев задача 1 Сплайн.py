import matplotlib.pyplot as plt
from math import *

def fun(x):
    if x>55:
        return 30 + cos(x)
    if x<=55:
        return 29
# + Задавайте присваиванием (здесь или раньше) 
a= 50
b= 60
n= 7
A= 12
B=-5

x=[]
y=[]
#коэффициенты 
# ξ и η - прогоночные коэффициенты
e=[]
h=[]
c=[]
o=(b-a)/n

for i in range(n+1):
    x.append(a+i*o)
    y.append(fun(x[i]))
    c.append(0)
    e.append(0)
    h.append(0)
print(x)


e[0]=0
h[0]=A
i = 1
while i < n:
    hi=x[i+1]-x[i]
    hi1=x[i]-x[i-1]
    e[i]=(-hi1/(e[i-1]*hi1+2*(x[i+1]-x[i-1])))
    h[i]=((6*((y[i+1]-y[i])/hi-(y[i]-y[i-1])/hi1) -h[i-1]*hi1) /(e[i-1]*hi1+2*(x[i+1]-x[i-1])))
    i += 1

c[n]=((y[n-1]-y[n])/(x[n]-x[n-1])**2 + B/(x[n]-x[n-1]))*3
i = n-1
while i>=0:
    c[i] = e[i]*c[i+1] + h[i]
    i -= 1
# поиск коэффициентов сплайна 

# построение сплайна
def Sp(t):
    i = 0
    while (x[i] > t)or(x[i+1] < t):
            i += 1
    #+Вне отрезка сплайн не определен, не надо продолжать
    hi=x[i+1]-x[i]
    return (y[i]*(x[i+1]-t)+(t-x[i])*y[i+1]) /hi + (c[i] *((x[i+1]-t)**3-hi**2*(x[i+1]-t)) +c[i+1]*((t-x[i])**3 -(t-x[i])*hi**2)) /(6*hi)



# производные на концах
def ddf(t):
    print(t)
    return [(1/(t**2))*(-2*Sp(a+t)+Sp(a)+Sp(a+2*t)),(1/(t**2))*(-2*Sp(b-t)+Sp(b)+Sp(b-2*t))]
def df(t):
    return [(1/t)*(Sp(a+t)-Sp(a)),(1/t)*(-Sp(b-t)+Sp(b))]

#+Здесь без обращения к подпрограммам найдите и распечатайте при разных эпсилон только требуемые производные на концах отрезка, т.е. в точках a  и b, а не  в x[0] и  x[n]


for i in range(6):
    t=10**(-i)
    print("Вторая производная на двух концах: ",ddf(t))
    print("Первая производная на двух концах: ",df(t))
    
xp = []
gr = []
grs = []
for i in range(20001):
    xp.append(a + i*(b-a)/20000)
    gr.append(fun(xp[i]))
    grs.append(Sp(xp[i]))

plt.scatter(x,y)
plt.plot(xp,gr)
plt.plot(xp,grs)
plt.show()
