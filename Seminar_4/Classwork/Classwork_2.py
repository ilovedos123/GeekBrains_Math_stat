# -*- coding: utf8 -*-
from scipy import stats
result = stats.norm.cdf(55, loc=30, scale=3) # loc - мат. ожидание; scale - сигма.
print(result)