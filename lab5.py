import matplotlib.pyplot as plt
import matplotlib.animation as anim
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
from sympy import*
import pylab

EPS = 0.00001
STEP_COUNT = 150
STEP_SIZE = 0.005 
X = np.array([i for i in np.linspace(-10, 10, 1000)])
Y = np.array([i for i in np.linspace(-10, 10, 1000)])

F = '4 * x ** 2 + 2 * x * y + 2.5 * y ** 2 - 6 * x - 7 * y + 2'

def func(X, Y):
    global F
    return eval(F.replace('x', str(X)).replace('y', str(Y)))
    return 4 * (X ** 2)  + 2.5 * (Y ** 2) + 2 * X * Y - 6 * X - 7 * Y + 2


def dx(x,y):
    xsym = Symbol('x')
    diff_x = str(diff(F,xsym))
    diff_x = diff_x.replace('x', str(x)).replace('y', str(y))
    diff_x = eval(diff_x)
    return diff_x
    
def d2x(x):
    xsym = Symbol('x')
    diff_x = str(diff(F,xsym))
    diff_x = str(diff(diff_x,xsym))
    diff_x = diff_x.replace('x', str(x))
    diff_x = eval(diff_x)
    return diff_x


def dy(x,y):
    ysym = Symbol('y')
    diff_y = str(diff(F,ysym))
    diff_y = diff_y.replace('y', str(y)).replace('x', str(x))
    diff_y = eval(diff_y)
    return diff_y

def d2y(y):
    ysym = Symbol('y')
    diff_y = str(diff(F,ysym))
    diff_y = str(diff(diff_y,ysym))
    diff_y = diff_y.replace('y', str(y))
    diff_y = eval(diff_y)
    return diff_y
    
def dxdy(x,y):
    ysym = Symbol('y')
    xsym = Symbol('x')
    diff_xy = str(diff(F,xsym))
    diff_xy = str(diff(diff_xy,ysym))
    diff_xy = diff_xy.replace('y', str(y))
    diff_xy = eval(diff_xy)
    return diff_xy
    
def dydx(x,y):
    ysym = Symbol('y')
    xsym = Symbol('x')
    diff_yx = str(diff(F,ysym))
    diff_yx = str(diff(diff_yx,xsym))
    diff_yx = diff_yx.replace('x', str(x))
    diff_yx = eval(diff_yx)
    return diff_yx

def gradient():
    global previous_x, previous_y, ax, num
    while(1):
        current_x = previous_x - STEP_SIZE * dx(previous_x, previous_y)
        current_y = previous_y - STEP_SIZE * dy(previous_x, previous_y)
        #print("Step:", num, "CurX:", current_x, "CurY", current_y, "Fun:", func(current_x, current_y))
        if(abs(func(current_x,current_y) - func(previous_x,previous_y)) < EPS):
           return [func(current_x, current_y), current_x, current_y, num]
        num = num + 1
        previous_x = current_x
        previous_y = current_y
    
    
def H(x,y):
    _d2y = d2y(y)
    _d2x = d2x(x)
    _dxdy = dxdy(x,y)
    _dydx = dydx(x,y)
    H = np.array([[_d2x, _dxdy],
            [_dydx,_d2y]] )
    return H
    
def newton():
    global previous_x, previous_y, num
    while(1):
        hrev = np.linalg.inv(H(previous_x, previous_y))
        p = -hrev @ [dx(previous_x, previous_y),dy(previous_x, previous_y)]
        current  = [previous_x, previous_y] + p
        #print("Step:", num, "CurX:", current[0], "CurY", current[1], "Fun:", func(current[0],current[1]))
        if abs(func(previous_x,previous_y) - func(current[0], current[1])) < EPS:
            return [func(current[0], current[1]),current[0], current[1],num]
        num = num + 1
        previous_x = current[0]
        previous_y = current[1]
        

def makeData ():
    x = np.arange (-10, 10, 0.1)
    y = np.arange (-10, 10, 0.1)
    xgrid, ygrid = np.meshgrid(x, y)

    zgrid = 4 * (xgrid) * (xgrid) + 16 * (ygrid) * (ygrid) + 4
    return xgrid, ygrid, zgrid

x, y, z = makeData()

fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, z, rstride=4, cstride=4, cmap = cm.jet)

pylab.show()

previous_x, previous_y = 8.8, 8.5
num = 0

newton_res = newton()

previous_x, previous_y = 8.8, 8.5
num = 0

gradient_res = gradient()
x,y = 8.8, 8.5
print("True Solution: F(x,y) = -3.6111111111111125  x =  0.4444444444444444  y =  1.2222222222222223")
print("Newton: F(x,y) = ", newton_res[0], " x = ", newton_res[1], " y = ", newton_res[2], ' iterations = ', newton_res[3] + 1)
print("Gradient: F(x,y) = ", gradient_res[0], " x = ", gradient_res[1], " y = ", gradient_res[2], " iterations = ", gradient_res[3] + 1,"\n\n")
