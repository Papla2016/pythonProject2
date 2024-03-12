from math import *
import pylab

def f1(x):
    return 2*sin(log(x**4))
def f2(x):
    return -cosh(x)/sinh(x)
def f(x):
    return 2*sin(log(x**4))+cosh(x)/sinh(x)
def fs(x):
    return ((8 * sinh(x)**2)*cos(4 * log(x)) - x) / (x * sinh(x)**2)
def fss(x):
    return -(32*sinh(x)**3*sin(4*log(x))+8*sinh(x)**3*cos(4*log(x))-2*x**2*cosh(x))/(x**2*sinh(x)**3)
def halfpart(i):
    a = i[0]
    b = i[1]
    j = 0
    ex = 0.0001
    c = (a + b) / 2
    while (abs(f(c)) > ex):
        if (j > 1000000):
            print("корни не найдены")
            return None
        if f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c
        c = (a + b) / 2
        j+=1
    return c
def bisec(i):
    a = i[0]
    b = i[1]
    eps = 0.0001
    if(f(a) * f(b) > 0):
        print("Корней нет")
        return None
    fa = f(a)
    fb = f(b)

    bn = b - (a - b) / (fa - fb) * fb

    while abs(b - bn) > eps:
        a = b
        b = bn
        fa = f(a)
        fb = f(b)
        if(f(i[0]) > 0):
            bn = b - (a - b) / (fa - fb) * fb
        else :
            bn = b - (a - b) / (fb - fa) * fa
    return bn
x = [i for i in range(2, 16)]
y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]
f3 = [f(i) for i in x]
z = []
count = 1
y = None
for i in f3:
    count = count + 1
    if y == None:
        y = i
    else:
        if (y < 0 and i > 0) or (y > 0 and i < 0):
            z.append([count-1,count])
        y = i
pylab.plot(x, y1)
pylab.figure(1)
pylab.plot(x, y2)
pylab.show()
z.append([7,8])
for i in z:
    print(f"Метод деления пополам для {i} и : " + str(halfpart(i)),end = "\n")
    print(f"метод хорд для {i}: " + str(bisec(i)),end ="\n")