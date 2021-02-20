from math import *

E = 10**(-12)
root = [0.73908513321516064166, 0]

a = 0
b = 1

i = 0

def f(x):
    return cos(x)-x

def df(x):
    return -sin(x)-1
M=1.84147
m=1
def rel():
    xp=b
    xn=a
    n=1
    while (root[i]-xn>E):
        print(n, xn,abs(root[i]-xn))
        xp = xn
        xn=xn-(2/(M+m))*f(xn)
        n+=1
  
    print(xn-xp)
            
    print(n, xn,abs(root[i]-xn))
    return xn
        
def bi():
    xl=a
    xr=b
    if f(xl)==0:
        print(xl)
    if f(xr)==0:
        print(xl)
    n=1
    while (abs(xl-xr)>E):
        print(n, xl,abs(root[i]-xl))
        xc=(xr-xl)/2
        xi=xl+xc
        if f(xl)*f(xi)<0:
            xr=xi
        else:
            xl=xi
        n+=1
    print(n, xl,abs(root[i]-xl))
    return xl

def s():
    xl=a
    xp=b
    n=1
    while abs(xl-xp)>=E:
        print(n, xl, abs(root[i]-xl))
        xn=xl-(f(xl)*(xl-xp)/(f(xl)-f(xp)))
        xp=xl
        xl=xn
        n+=1
    print(n, xl, abs(root[i]-xl))
    return xl

def h():
    xl = b
    if xl == a:
        xc = b
    else:
        xc = a
    xp = xc
    n = 1
    while (abs(xl - xp) >= E):
        print(n, xl, abs(root[i]-xl))
        xp = xl
        xl = f(xc)*(xc - xl)/(f(xl)-f(xc)) + xc
        n += 1
    print(n, xl, abs(root[i]-xl))
    return xl

def n():
    xl = b
    xp = a
    n = 1
    while (abs(f(xl)/df(xl)) >= E):
        print(n, xl, abs(root[i]-xl))
        xp = xl
        xl = xl - f(xl)/df(xl)
        n += 1
    print(n, xl, abs(root[i]-xl))
    return xl

