# -*- mode: python ; coding: utf-8 -*-
# Задача 3 Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2. Найдите доверительный интервал для
# математического  ожидания с надежностью 0.95.
n = 27
M = 174.2
dispersion = 25
sigma = dispersion**(1/2)
# Так как дисперсия генеральной совокупности известна, то используем Z критерий. По таблице для альфа/2 Z = 1,96.
Z = 1.96
value_1 = M - Z * (sigma/n**0.5)
value_2 = M + Z * (sigma/n**0.5)
print(f'Доверительный интервал: [{value_1}; {value_2}]')
