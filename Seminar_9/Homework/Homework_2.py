# -*- mode: python ; coding: utf-8 -*-
# Задача 2 Посчитать коэффициент линейной регрессии при заработной плате (zp), используя
# градиентный спуск (без intercept).
import numpy

zp = numpy.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = numpy.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
alpha = 1e-6
coeff_b = 0.1
def mse(coeff_b, y=ks, X=zp, n=10):
    return numpy.sum((coeff_b * X - y) ** 2) / n
for i in range(1000):
    fp = (1 / 10) * numpy.sum(2 * (coeff_b * zp - ks) * zp)
    coeff_b -= alpha * fp
    if i % 100 == 0:
        print(f'Итерация: {i}, Коэффициент b : {coeff_b}, mse: {mse(coeff_b) }')
print('Коэффициент b = 5.889820420065112')

