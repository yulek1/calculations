# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt

def f1(t):
    return 2.94 * np.power(t, 1.09) # dob komp v shablon, mod = 0,1 osn

def f2(t):
    return 2.94 * np.power(5*t, 1.07) # mod komp

def f3(t):
    return 2.94 * np.power(2.5*t, 1.07) # mod komp

matplotlib.rcdefaults()
matplotlib.rcParams['font.family'] = 'fantasy'
matplotlib.rcParams['font.fantasy'] = 'Times New Roman', 'Ubuntu','Arial','Tahoma','Calibri'

t1 = np.arange(0.0, 4.0, 0.1)
x_begin = 1
x_end = 2
y_lim = 70

plt.figure(figsize = (16,4))

sp = plt.subplot(1,3,1)

plt.xlabel(u"KLOC, тыс. строк/компонент", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)

plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)

plt.plot(t1, f1(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Базовое", fontsize=18)

plt.axvspan(x_begin, x_end, color='grey', alpha=0.3)
plt.axhspan(f1(x_begin), f1(x_end), color='grey', alpha=0.3)
plt.grid()

sp1 = plt.subplot(1,3,2)
plt.xlabel(u"KLOC, тыс. строк/компонент", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)

plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)

plt.plot(t1, f2(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Худший сценарий", fontsize=18)

plt.axvspan(x_begin, x_end, color='grey', alpha=0.3)
plt.axhspan(f2(x_begin), f2(x_end), color='grey', alpha=0.3)
plt.grid()

sp2 = plt.subplot(1,3,3)
plt.xlabel(u"KLOC, тыс. строк/компонент", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)

plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)

plt.plot(t1, f3(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Обычный сценарий", fontsize=18)

plt.axvspan(x_begin, x_end, color='grey', alpha=0.3)
plt.axhspan(f3(x_begin), f3(x_end), color='grey', alpha=0.3)

plt.grid()
plt.tight_layout()
plt.savefig('modif.png')
