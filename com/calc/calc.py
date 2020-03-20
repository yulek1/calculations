# -*- coding: utf-8 -*-

import numpy as np

import matplotlib as matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt

def f1(t):
    return 2.94 * np.power(t, 1.03) #dob komp v shablon

matplotlib.rcdefaults()
matplotlib.rcParams['font.family'] = 'fantasy'
matplotlib.rcParams['font.fantasy'] = 'Times New Roman', 'Ubuntu','Arial','Tahoma','Calibri'

t1 = np.arange(0.0, 4.0, 0.1)

x_begin = 1
x_end = 2
y_lim = 15

plt.figure(1)
plt.title(u"Базовое", fontsize=18)
plt.xlabel(u"KLOC, тыс. строк/компонент", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)

plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)

plt.plot(t1, f1(t1), 'k')
plt.ylim((0,y_lim))
plt.axvspan(x_begin, x_end, color='grey', alpha=0.3)
plt.axhspan(f1(x_begin), f1(x_end), color='grey', alpha=0.3)
plt.grid()


plt.savefig('base.png')
