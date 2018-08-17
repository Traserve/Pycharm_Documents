import pandas as pd

# Python读取csv文件操作
# https://www.cnblogs.com/zzhzhao/p/5269217.html
# https://blog.csdn.net/Flying_sfeng/article/details/58596978

df = pd.read_csv('seaborn-data\\tips.csv')
# print(df.head()) # 打印数据前5行
# print(df.tail()) # 打印数据后5行

print(df.columns)  # 打印列名
# print(df.columns[2])
# print(df.index) # 打印列信息

# print(df.ix[10:20, 0:3]) # 打印10~20行前三列数据
# print(df.iloc[[1,3,5], [2,4]]) # 提取不连续行和列的数据，这个例子提取的是第1,3,5行，第2,4列的数据
# print(df.iat[3, 2]) # 专门提取某一个数据，这个例子提取的是第三行，第二列数据（默认从0开始算哈）

# print(df.drop([df.columns[0],df.columns[1]], axis = 1)) # 舍弃两列数据
# print(df.drop(['total_bill', 'tip'], axis = 1)) # 舍弃两列数据
# print(df.drop(columns=['total_bill', 'tip'], axis = 1)) # 舍弃两列数据
# print(df.drop([0, 1], axis = 0)) # 舍弃两行数据
# print(df.drop([0, 1])) # 舍弃两行数据

# print(df.shape) # 打印维度
# print(df.iloc[3]) # 打印第3行
# print(df.iloc[2:5]) # 选取第2到第4行
# print(df.iloc[0,1]) # 选取第0行1列的元素

# print(df[df.tip > 8]) # 筛选出小费大于$8的数据
# 数据筛选同样可以用”或“和”且“作为筛选条件
# print(df[(df.tip>7) | (df.total_bill>50)]) # 筛选出小费大于$7或总账单大于$50的数据
# print(df[(df.tip>7) & (df.total_bill>50)]) # 筛选出小费大于$7且总账单大于$50的数据
# 加入筛选条件
# print(df[['day','time']][(df.tip>7)|(df.total_bill>50)])

# print(df.describe()) # 统计描述

# print(df.T) # 数据转置

# print(df.sort_values(by='tip'))  # 按tip列升序排序

# group = df.groupby('day') # 按day这一列进行分组
# print(group.first()) # 打印每一组的第一行数据
# print(group.last()) # 打印每一组的最后一行数据
