# -*- coding: utf-8 -*-
# %matplotlib inline
import numpy as np
import matplotlib as matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt

I=0.4

def f1(t):
    return 2.94 * (np.power(205*t, 1.09)+(np.power(8*205*t*I, 1.07))+(np.power(t, 1.07)))

K=0.5

def f2(t):
    return 2.94 * (np.power(205*t, 1.09)+(np.power(8*205*t*K, 1.07))+(np.power(t, 1.07)))

M=0.6

def f3(t):
    return 2.94 * (np.power(205*t, 1.09)+(np.power(8*205*t*M, 1.07))+(np.power(t, 1.07)))

x_begin = 0.5
x_end = 2.5
y_lim = 20000

matplotlib.rcdefaults()
matplotlib.rcParams['font.family'] = 'fantasy'
matplotlib.rcParams['font.fantasy'] = 'Times New Roman', 'Ubuntu','Arial','Tahoma','Calibri'

t1 = np.arange(0.0, 6.0, 0.1)

plt.figure(figsize = (16,4))

sp = plt.subplot(1,3,1)


plt.xlabel(u"KLOC, тыс. строк/компонент", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.plot(t1, f1(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Минимальное", fontsize=18)
plt.grid()
plt.axvspan(x_begin, x_end, color='grey', alpha=0.3)
plt.axhspan(f1(x_begin), f1(x_end), color='grey', alpha=0.3)

plt.axhspan(2403, 2403, color='black', alpha=1)

sp1 = plt.subplot(1,3,2)
plt.xlabel(u"KLOC, тыс. строк/компонент", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.plot(t1, f2(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Усредненное", fontsize=18)

plt.axvspan(x_begin, x_end, color='grey', alpha=0.4)
plt.axhspan(f2(x_begin), f2(x_end), color='grey', alpha=0.4)

plt.grid()
plt.axhspan(2403, 2403, color='black', alpha=1)

sp1 = plt.subplot(1,3,3)
plt.xlabel(u"KLOC, тыс. строк/компонент", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.plot(t1, f3(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Максимальное", fontsize=18)

plt.axvspan(x_begin, x_end, color='grey', alpha=0.3)
plt.axhspan(f3(x_begin), f3(x_end), color='grey', alpha=0.3)

plt.grid()
plt.axhspan(2404, 2404, color='black', alpha=1)
plt.tight_layout()

plt.savefig('evaluation_real.png')
