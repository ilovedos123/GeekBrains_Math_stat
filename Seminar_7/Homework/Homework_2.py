# -*- mode: python ; coding: utf-8 -*-
# Задача 2. Исследовалось влияние препарата на уровень давления пациентов. Сначала
# измерялось давление до приема препарата, потом через 10 минут и через 30 минут. Есть
# ли статистически значимые различия между измерениями давления? В выборках не соблюдается условие нормальности.
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150, 130, 135
# 3е измерение через 30 минут: 130, 130, 120, 130, 125
import scipy.stats as stats
x1 = [150, 160, 165, 145, 155]
x2 = [140, 155, 150, 130, 135]
x3 = [130, 130, 120, 130, 125]
#Так как выборок ,больше двух и они зависимые (на одного пациента, несколько замеров), то для сравнения выбираем критерий Фридмана.
print(stats.friedmanchisquare(x1, x2, x3))
# При альфа = 0,05: 0,008 < 0,05. Отвергаем Но. Статистически значимые различия между группами есть. Препарат влияет на уровень давления.