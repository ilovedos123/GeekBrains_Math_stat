# -*- mode: python ; coding: utf-8 -*-
# Задача 3 (Дополнительно) Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что
# изменение коэффициентов должно производиться
# на каждом шаге одновременно (то есть изменение одного коэффициента не должно
# влиять на изменение другого во время одной итерации).
import numpy
zp = numpy.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = numpy.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
def mse_ab(a, b, x, y):
    return numpy.sum(((a + b * x)-y)**2)/len(x)
def mse_pa(a, b, x, y):
    return 2*numpy.sum((a + b * x)-y)/len(x)
def mse_pb(a, b, x, y):
    return 2*numpy.sum((( a + b * x)-y)*x)/len(x)
alpha = 5e-05
coeff_b = 0.1
coeff_a = 0.1
i_min = 1
b_min = coeff_b
a_min = coeff_a
mseab_min = mse_ab(coeff_a, coeff_b, zp, ks)
for i in range(1000000):
    coeff_a -= alpha*mse_pa(coeff_a, coeff_b, zp, ks)
    coeff_b -= alpha*mse_pb(coeff_a, coeff_b, zp, ks)
    if i % 50000 == 0:
        print(f'Коэффициент a = {coeff_a}, коэффициент b = {coeff_b}, mse = {mse_ab(coeff_a, coeff_b, zp,ks)}')
    if mse_ab(coeff_a, coeff_b, zp, ks) > mseab_min:
        print(f'Коэффициент a = {a_min}, коэффициент b = {b_min}, mse = {mseab_min}')
        break
    else:
        mseab_min = mse_ab(coeff_a, coeff_b, zp, ks)
        i_min = i
        b_min = coeff_b
        a_min = coeff_a
    print(f'Итерация #{i}, a = {a_min} b = {b_min}')