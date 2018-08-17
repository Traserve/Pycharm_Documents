import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
from scipy import stats

# 独立样本t检验
IS_t_test = pd.read_excel('seaborn-data\\t_test.xlsx')
Group1 = IS_t_test[IS_t_test['group'] == 1]['data']
Group2 = IS_t_test[IS_t_test['group'] == 2]['data']
# 独立样本t检验
# print(ttest_ind(Group1, Group2))
# 输出结果的第一个元素为t值，第二个元素为p-value
# ttest_ind默认两组数据方差齐性的，如果想要设置默认方差不齐，可以设置equal_var=False
# print(ttest_ind(Group1, Group2, equal_var=True))
# print(ttest_ind(Group1, Group2, equal_var=False))

# 配对样本t检验
# print(ttest_rel(Group1, Group2))

# levene方差齐性检验。levene(*args, **kwds) 果p<0.05，则方差不齐
# w,p = stats.levene(*args)
# print(w,p)
# 进行方差分析
# f,p = stats.f_oneway(*args)
# print(f,p)
