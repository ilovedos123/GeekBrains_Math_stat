from scipy import stats
result = stats.norm.cdf(45, loc=50, scale=3) # loc - ���. ��������; scale - �����.
print(result)