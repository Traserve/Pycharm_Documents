import pandas as pd

# 值替换
Series = pd.Series([0, 1, 2, 3, 4, 5])
# print(Series)
print(Series.replace(0, 100000000))  # 数值替换，例如将0换成10000000000000
print(Series.replace([0, 1, 2, 3, 4, 5], [111, 222, 333, 444, 555, 666]))  # 列和列的替换同理
