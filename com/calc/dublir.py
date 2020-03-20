# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def f1(t):
    return 2.94 * np.power(t, 1.09) # dob komp v shablon

def f2(t):
    return 2.94 * np.power(t, 1.07) # dublir

matplotlib.rcdefaults()
matplotlib.rcParams['font.family'] = 'fantasy'
matplotlib.rcParams['font.fantasy'] = 'Times New Roman', 'Ubuntu','Arial','Tahoma','Calibri'

t1 = np.arange(0.0, 4.0, 0.1)
t2 = 0.2*t1

x_begin = 1
x_end = 2
y_lim = 20


plt.figure(figsize = (16,4))

sp = plt.subplot(1,3,1)

plt.xlabel(u"KLOC, тыс. строк", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)
plt.plot(t1, f1(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Базовое", fontsize=18)

plt.axvspan(x_begin, x_end, color='gray', alpha=0.4)
plt.axhspan(f1(x_begin), f1(x_end), color='gray', alpha=0.4)
plt.grid()

sp1 = plt.subplot(1,3,2)
plt.xlabel(u"KLOC, тыс. строк/компонент", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)
plt.plot(t1, f2(t1), 'k')
plt.ylim((0,y_lim))
plt.title(u"Дублирование компонента - худший сценарий", fontsize=18)

plt.axvspan(x_begin, x_end, color='gray', alpha=0.4)
plt.axhspan(f2(x_begin), f2(x_end), color='gray', alpha=0.4)
plt.grid()

sp2 = plt.subplot(1,3,3)
plt.xlabel(u"KLOC, тыс. строк/компонент", fontsize=18)
plt.ylabel(u"Трудоемкость, чел-мес", fontsize=18)
plt.plot(t1, f2(t2), 'k')
plt.ylim((0,10))
plt.title(u"Дублирование компонента - обычный сценарий", fontsize=18)

plt.axvspan(x_begin, x_end, color='gray', alpha=0.4)
plt.axhspan(f2(x_begin*0.2), f2(x_end*0.2), color='gray', alpha=0.4)
plt.tight_layout()
plt.grid()

plt.savefig('dublir.png')

