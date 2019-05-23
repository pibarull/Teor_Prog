# -*- coding: utf-8 -*-

import numpy as np

# число точек
N = 10000;

fundel = 100;
# пределы
R = 1;
x1 = -R;
x2 = R;
y1 = -R;
y2 = R;
func = lambda x, y: 2 * (x ** 2) + 1 * (y ** 2)

# поиск максимума
fmax = 0;
for i in range(fundel + 1):
    ny = np.sqrt(1 - ((i * (x2 - x1) / fundel) + x1) ** 2)
    ny1 = -ny
    ny2 = ny
    for j in range(fundel + 1):

        if func((i * (x2 - x1) / fundel) + x1, (j * (ny2 - ny1) / fundel) + ny1) > fmax:
            fmax = func((i * (x2 - x1) / fundel) + x1, (j * (ny2 - ny1) / fundel) + ny1)
sum = 0
for i in range(N):
    xcor = (x2 - x1) * np.random.sample() + x1
    ym = np.sqrt(1 - xcor ** 2)
    ycor = (2 * ym) * np.random.sample() - ym

    # print(xcor,' - ',ycor,' - ', xcor**2+ycor**2)
    zcor = fmax * np.random.sample()
    if func(xcor, ycor) >= zcor:
        sum += 1

res = np.pi * (R ** 2) * fmax * sum / N
print(res)
# -*- coding: utf-8 -*-

import numpy as np

# число точек
N = 10000;

fundel = 100;
# пределы
R = 1;
x1 = -R;
x2 = R;
y1 = -R;
y2 = R;
func = lambda x, y: 2 * (x ** 2) + 1 * (y ** 2)

# поиск максимума
fmax = 0;
for i in range(fundel + 1):
    ny = np.sqrt(1 - ((i * (x2 - x1) / fundel) + x1) ** 2)
    ny1 = -ny
    ny2 = ny
    for j in range(fundel + 1):

        if func((i * (x2 - x1) / fundel) + x1, (j * (ny2 - ny1) / fundel) + ny1) > fmax:
            fmax = func((i * (x2 - x1) / fundel) + x1, (j * (ny2 - ny1) / fundel) + ny1)
sum = 0
for i in range(N):
    xcor = (x2 - x1) * np.random.sample() + x1
    ym = np.sqrt(1 - xcor ** 2)
    ycor = (2 * ym) * np.random.sample() - ym

    # print(xcor,' - ',ycor,' - ', xcor**2+ycor**2)
    zcor = fmax * np.random.sample()
    if func(xcor, ycor) >= zcor:
        sum += 1

res = np.pi * (R ** 2) * fmax * sum / N
print(res)
