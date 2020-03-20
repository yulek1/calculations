# -*- coding: utf-8 -*-
# %matplotlib inline
import numpy as np
import matplotlib as matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt


I=0.3

def f1(t):
    return 2.94 * (np.power(205*t, 1.653)+(np.power(8*205*t*I, 1.56))+((np.power(9, 1.49)+np.power(7*I, 1.49))*(np.power(t, 1.49))))

K=0.45

def f2(t):
    return 2.94 * (np.power(205*t, 1.653)+(np.power(8*205*t*K, 1.56))+((np.power(9, 1.49)+np.power(7*K, 1.49))*(np.power(t, 1.49))))

M=0.5

def f3(t):
    return 2.94 * (np.power(205*t, 1.653)+(np.power(8*205*t*M, 1.56))+((np.power(9, 1.49)+np.power(7*M, 1.49))*(np.power(t, 1.49))))

x_begin = 0.5
x_end = 2.5
y_lim = 650000

matplotlib.rcdefaults()
matplotlib.rcParams['font.family'] = 'fantasy'
matplotlib.rcParams['font.fantasy'] = 'Times New Roman', 'Ubuntu','Arial','Tahoma','Calibri'

t1 = np.arange(0.0, 6.0, 0.1)

plt.figure(figsize = (16,4))

sp = plt.subplot(1,3,1)

plt.xlabel(u"KLOC, тыс. строк/компонент", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)
plt.plot(t1, f1(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Минимальное")

plt.axvspan(x_begin, x_end, color='gray', alpha=0.4)
plt.axhspan(f1(x_begin), f1(x_end), color='gray', alpha=0.4)
plt.grid()

sp1 = plt.subplot(1,3,2)
plt.xlabel(u"KLOC, тыс. строк/компонент")
plt.ylabel(u"Трудоемкость, чел-мес")
plt.plot(t1, f2(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Усредненное")

plt.axvspan(x_begin, x_end, color='gray', alpha=0.4)
plt.axhspan(f2(x_begin), f2(x_end), color='gray', alpha=0.4)
plt.grid()

sp1 = plt.subplot(1,3,3)
plt.xlabel(u"KLOC, тыс. строк/компонент")
plt.ylabel(u"Трудоемкость, чел-мес")
plt.plot(t1, f3(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Максимальное")

plt.axvspan(x_begin, x_end, color='gray', alpha=0.4)
plt.axhspan(f3(x_begin), f3(x_end), color='gray', alpha=0.4)
plt.grid()

print(f1(x_begin))
print(f3(x_end))
plt.savefig('evaluation.png')
