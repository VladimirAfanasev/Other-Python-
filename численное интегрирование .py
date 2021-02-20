import math
def F(x):
    return 1/(1+x**2)

def Pr(x,h,n):
    p=0
    for i in range(n):
        p+=F((x[i+1]+x[i])/2)*(x[i+1]-x[i])
    return p
def Gaus2(x,n):
    p=0
    for i in range(n):
        p+=((x[i+1]-x[i])/2)*(F(((x[i]+x[i+1])/2)-((x[i+1]-x[i])/(2*math.sqrt(3))))+F(((x[i]+x[i+1])/2)+((x[i+1]-x[i])/(2*math.sqrt(3)))))
    return p  


n=int(input('Введите колличество интервалов '))

a=-5
b=5

h=float((b-a)/n)
x=[a]
for i in range(n):
    x.append(x[i]+h)

    #for i in range(n):
        #x[i]=(a+b)/2 + ((b-a)/2)*math.cos((2*(i+1)-1)*math.pi/(2*n))
    #print(x)
print(n)
print('Метод прямоугольников: ',Pr(x,h,n),'|  Метод Гаусса: ',Gaus2(x,n))
        

x2=[a]
h2=float((b-a)/(2*n))
for i in range(n*2):
    x2.append(x2[i]+h2)
x4=[a]
h4=float((b-a)/(4*n))
for i in range(n*4):
    x4.append(x4[i]+h4)

def AlPr():
    print('Степень точности прямоугольника: ', math.log2((Pr(x,h,n)-Pr(x2,h2,n*2))/(Pr(x2,h2,n*2)-Pr(x4,h4,n*4)))-1)
def AlG():
    print('Степень точности Гаусса: ', math.log2((Gaus2(x,n)-Gaus2(x2,n*2))/(Gaus2(x2,n*2)-Gaus2(x4,n*4)))-1)
    
