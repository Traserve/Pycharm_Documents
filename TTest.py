import pandas as pd
from scipy.stats import ttest_ind

# 独立样本t检验
IS_t_test = pd.read_excel('seaborn-data\\t_test.xlsx')
Group1 = IS_t_test[IS_t_test['group'] == 1]['data']
Group2 = IS_t_test[IS_t_test['group'] == 2]['data']
print(ttest_ind(Group1, Group2))
# 输出结果的第一个元素为t值，第二个元素为p-value
# ttest_ind默认两组数据方差齐性的，如果想要设置默认方差不齐，可以设置equal_var=False
print(ttest_ind(Group1, Group2, equal_var=True))
print(ttest_ind(Group1, Group2, equal_var=False))
