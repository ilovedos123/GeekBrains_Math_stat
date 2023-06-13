# -*- mode: python ; coding: utf-8 -*-
# Задача 3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175#
# Используя эти данные построить 95% доверительный интервал для разности среднего
# роста родителей и детей.

daughters = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
mothers = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
alpha = 0.05
X_daughters = sum(daughters)/len(daughters)
X_mothers = sum(mothers)/len(mothers)
delta = X_daughters - X_mothers
if delta < 0:
    delta = delta * -1
numerator = 0
for i in daughters:
    numerator = numerator + (i - X_daughters)**2
dispersion_daughters = numerator/(len(daughters)-1)
numerator = 0
for i in mothers:
    numerator = numerator + (i - X_mothers)**2
dispersion_mothers = numerator/(len(mothers)-1)
S_delta = ((dispersion_daughters/len(daughters)) + (dispersion_mothers/len(mothers)))**0.5
# Так как выборки две, по таблице для альфа/2, при 2(n-1) степеней свободы t = 2,131.
t = 2.131
value_1 = delta - t * S_delta
value_2 = delta + t * S_delta
print(f'Доверительный интервал: [{value_1}; {value_2}]')