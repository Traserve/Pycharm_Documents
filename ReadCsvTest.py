import pandas as pd

# https://www.cnblogs.com/zzhzhao/p/5269217.html
# https://blog.csdn.net/Flying_sfeng/article/details/58596978

df = pd.read_csv('D:\\PycharmProjects\\tips.csv')
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
# print(df.iloc[2:5]) # 选取第2到第3行
# print(df.iloc[0,1]) # 选取第0行1列的元素

print(df.tip > 8)
