import json
import numpy as np
import pandas as pd
from pandas import DataFrame

# Python对缺省值处理
path = 'seaborn-data\\example.txt'
records = [json.loads(line) for line in open(path)]  # 转化为Python的字典对象
frame = DataFrame(records)
# print(frame['tz'])
# 替换的值只是缺失值并不是为空的值，如：序号13行{"_heartbeat_":1331923261}，缺失值不进行替换打印的时候显示为NaN
# print(frame['tz'].fillna(1111111111111))  # 以数字代替缺失值
# print(frame['tz'].fillna('////////////')) # 用字符串代替缺失值
# print(frame['tz'].fillna(method='pad'))   # 用前一个数据代替缺失值
# print(frame['tz'].fillna(method='bfill')) # 用后一个数据代替缺失值
# print(frame['tz'].dropna(axis=0)) # 删除缺失行
# print(frame['tz'].dropna(axis=1)) # 删除缺失列

# 插值法填补缺失值
# 创建一个6*4的数据框，randn函数用于创建随机数
czf_data = pd.DataFrame(np.random.rand(6, 4), columns=list('ABCD'))
# print(czf_data)
# 把第二列数据设置为缺失值
czf_data.ix[2, :] = np.nan
# print(czf_data)
# 利用插值法填补空缺值
print(czf_data.interpolate())
