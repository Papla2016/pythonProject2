from math import *
import pylab


def f1(x):
    return 6/(sqrt(5 + 4*x - x**2))
def fs1(x):
    return -(6*x-12)/(sqrt((-x**2)+4*x+5)*(x**2-4*x-5))
def f2(x):
    return cos(log(x))
def fs2(x):
    return -sin(log(x))/x
def f(x):
    return 2*sin(log(x**4))+cosh(x)/sinh(x)
def fs(x):
    return (8*sinh(x)**2*cos(4*log(x))-x)/(x*sinh(x)**2)
def fss(x):
    return -(32*sinh(x)**3*sin(4*log(x))+8*sinh(x)**3*cos(4*log(x))-2*x**2*cosh(x))/(x**2*sinh(x)**3)
def rect_integral(f,fs,xmin,xmax,n):
    h=(xmax-xmin)/n
    area=0
    x=xmin
    m = max(fs(x) for x in range(xmin,xmax))
    for i in range(n):
        area+=h*f(x)
        x+=h
    ex = ((xmax - xmin) * h ** 2) / 24 * m
    return area,ex
def f3(x):
    return log(x)
def f3s(x):
    return 1/x
def f3ss(x):
    return -1/(x**2)
def f3sss(x):
    return 2/(x**3)
def f3ssss(x):
    return -6/(x**4)


def tangent(x,x0):
    return fs(x)*(x-x0)+f(x0)
def newton_method(x0,epsilon):
    while True:
        fx0 = f(x0)
        if abs(fx0) < epsilon:
            return x0
        x0 = x0 - fx0 / fs(x0)
def find_roots(i, epsilon):
    left = i[0]
    right = i[1]
    a = left
    while a < right:
        if f(a) * f(a + epsilon) < 0:
            root = newton_method(a, epsilon)
            return root
        a += epsilon
    return None


def halfpart(i,ex):
    a = i[0]
    b = i[1]
    j = 0

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

def bisec(i,eps):
    a = i[0]
    b = i[1]
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
        bn = b - (a - b) / (fa - fb) * fb

    return bn

def trapezoid_method(f,fs, a, b, n):
    h = (b - a) / n
    res = h * (0.5 * f(a) + 0.5 * f(b) + sum(f(a + i * h) for i in range(1, n)))
    max_derivative = max(fs(x) for x in range(a, b + 1))
    error = (b - a) * h ** 2 / 12 * max_derivative
    return res, error
def simpson_rule(f,f4, a, b, n):
    h = (b - a) / n
    integral = h / 3 * (f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 2 * sum(f(a + i * h) for i in range(2, n, 2)))
    ma = max(f4(x) for x in range(a,b+1))
    ex = ((b-a)*h**4)/180 * ma
    return integral, ex
"""
x = [i for i in range(2, 16)]
y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]
f3 = [f(i) for i in x]
f4 = [fs(i) for i in x]
zero = [0 for i in x]
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
pylab.plot(x, f3)
pylab.figure(1)
pylab.plot(x, y2)
pylab.plot(x,f4)
pylab.show()
z.append([7,8])
"""
rez,e = trapezoid_method(f,f3ss,1,5,1000)
print(f"Результат работы трапеции - {rez}\nТочность - {e}")
res, ex = simpson_rule(f,f3ssss,1,5,100)
print(f"Результат работы метода симпсона - {res}\nТочность - {ex}")
"""
for i in z:
    print(f"Метод деления пополам для {i} и : " + str(halfpart(i,eps)),end = "\n")
    print(f"метод хорд для {i}: " + str(fs(bisec(i,eps))),end ="\n")
    print(f"Метод Ньютона для {i}: " + str(find_roots(i,eps)),end = "\n")
"""