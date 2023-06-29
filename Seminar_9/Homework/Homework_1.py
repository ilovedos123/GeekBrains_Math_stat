# -*- mode: python ; coding: utf-8 -*-
# Задача 1 Даны значения величины заработной платы заемщиков банка (zp) и значения их
# поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Используя математические
# операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату
# (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая
# переменная). Произвести расчет как с использованием intercept, так и без.
import numpy
import matplotlib.pyplot

zp = numpy.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = numpy.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
matplotlib.pyplot.scatter(zp,ks)
matplotlib.pyplot.show()
coeff_b = ((zp * ks).mean() - zp.mean() * ks.mean()) / ((zp ** 2).mean() - (zp.mean() ** 2))
print(f'Коэффициент b равен {coeff_b}')
coeff_a = ks.mean() - coeff_b * zp.mean()
print(f'Коэффициент a равен {coeff_a}')
matplotlib.pyplot.scatter(zp,ks)
matplotlib.pyplot.plot(zp, coeff_a+coeff_b*zp)
matplotlib.pyplot.show()

# c intercept
zp = numpy.vstack([numpy.ones((1, 10)), zp])
print(numpy.dot(numpy.dot(numpy.linalg.inv(numpy.dot(zp, zp.T)), zp), ks.T))

# без c intercept
zp = numpy.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = numpy.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
zp = zp.reshape(1, len(zp))
ks = ks.reshape(1, len(ks))
print(numpy.dot(numpy.dot(numpy.linalg.inv(numpy.dot(zp, zp.T)), zp), ks.T))
