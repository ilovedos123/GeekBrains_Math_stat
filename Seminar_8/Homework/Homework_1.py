# -*- mode: python ; coding: utf-8 -*-
# Задача 1 Даны значения величины заработной платы заемщиков банка (zp) и значения их
# поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с
# помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и
# среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

import numpy

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]
M_zp = sum(zp)/len(zp)
M_ks = sum(ks)/len(ks)
M_zp_ks = (sum(numpy.array(zp)*numpy.array(ks))/len(numpy.array(zp)*numpy.array(ks)))
cov = M_zp_ks - M_zp * M_ks
print(cov)
print(numpy.cov(zp, ks, ddof = 0))

X = sum(zp)/len(zp)
numerator = 0
for i in zp:
    numerator = numerator + (i - X)**2
dispersion = numerator/(len(zp))
sigma_zp = dispersion**(1/2)
X = sum(ks)/len(ks)
numerator = 0
for i in ks:
    numerator = numerator + (i - X)**2
dispersion = numerator/(len(ks))
sigma_ks = dispersion**(1/2)
corrcoef = cov / (sigma_zp * sigma_ks)
print(corrcoef)
print(numpy.corrcoef(zp, ks))

