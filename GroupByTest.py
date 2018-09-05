import numpy as np
import pandas as pd
import statsmodels.api as sm

# print(pd.get_option('display.width'))
# print(pd.get_option('display.max_columns'))
pd.set_option('display.width', 500)  # 默认80
pd.set_option('display.max_columns', 50)

# 分组运算
# "split-apply-combine"（拆分－应用－合并）。
# 第一个阶段，pandas对象（无论是Series、DataFrame还是其他的）中的数据会根据你所提供的一个或多个键被拆分（split）为多组。
# 拆分操作是在对象的特定轴上执行的。例如，DataFrame可以在其行（axis=0）或列（axis=1）上进行分组。
# 然后，将一个函数应用（apply）到各个分组并产生一个新值。
# 最后，所有这些函数的执行结果会被合并（combine）到最终的结果对象中。结果对象的形式一般取决于数据上所执行的操作
# 例如分组求和：根据相应条件对原数据进行分组(split)，应用求和函数sum，最后合并称一条数据

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})
# grouped = df['data1'].groupby(df['key1'])
# # print(grouped.mean())
# means = df['data1'].groupby([df['key1'], df['key2']]).mean()
# sizes = df['data1'].groupby([df['key1'], df['key2']]).size()
# print(means)
# print(sizes)

# for name, group in df.groupby('key1'):
#     print(name)
#     print(group)

# for (k1,k2), group in df.groupby(['key1', 'key2']):
#     print((k1, k2))
#     print(group)

# 将这些数据片段做成一个字典
# pieces = dict(list(df.groupby('key1')))
# print(pieces['b'])

# groupby默认是在axis=0上进行分组的，通过设置也可以在其他任何轴上进行分组。拿上面例子中的df来说，我们可以根据dtype对列进行分组
# print(df.dtypes)
# grouped = df.groupby(df.dtypes, axis=1)
# for dtype, group in grouped:
#     print(dtype)
#     print(group)

# 尤其对于大数据集，很可能只需要对部分列进行聚合。例如，在前面那个数据集中，如果只需计算data2列的平均值并以DataFrame形式得到结果，可以这样写
# groupde1 = df.groupby(['key1', 'key2'])[['data2']].mean()  # 这种索引操作所返回的对象是一个已分组的DataFrame（如果传入的是列表或数组）或已分组的Series
# s_grouped = df.groupby(['key1', 'key2'])['data2'].mean()  # 如果传入的是标量形式的单个列名
# print(groupde1)
# print(s_grouped)


people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.iloc[2:3, [1, 2]] = np.nan
# print(people)
# 存在未使用的分组键是可以的
mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f': 'orange'}
# by_column = people.groupby(mapping, axis=1)
# print(by_column.sum())
# Series也有同样的功能，它可以被看做一个固定大小的映射
# map_series = pd.Series(mapping)
# print(map_series)
# print(people.groupby(map_series, axis=1).count())

# 索引值为人的名字的字符串长度
# print(people.groupby(len).sum())

# 将函数跟数组、列表、字典、Series混合使用也不是问题，因为任何东西在内部都会被转换为数组
# key_list = ['one', 'one', 'one', 'two', 'two']
# print(people.groupby([len, key_list]).min())

# 层次化索引数据集最方便的地方就在于它能够根据轴索引的一个级别进行聚合：
# columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
#                                      [1, 3, 5, 1, 3]],
#                                     names=['cty', 'tenor'])
# hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)
# print(hier_df)
# print(hier_df.groupby(level='cty', axis=1).count())

grouped = df.groupby('key1')
# print(grouped['data1'].quantile(0.9))

# 如果要使用你自己的聚合函数，只需将其传入aggregate或agg方法即可
def peak_to_peak(arr):
    return arr.max() - arr.min()
# print(grouped.agg(peak_to_peak))
# 有些方法（如describe）也是可以用在这里的，即使严格来讲，它们并非聚合运算
# print(grouped.describe())

tips = pd.read_csv('seaborn-data\\tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
# print(tips[:6])

grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped['tip_pct']
# 可以将函数名以字符串的形式传入
# print(grouped_pct.agg('mean'))
# print(grouped_pct.agg(['mean', 'std', peak_to_peak]))
# 对于DataFrame，你还有更多选择，你可以定义一组应用于全部列的一组函数，或不同的列应用不同的函数
# functions = ['count', 'mean', 'max']
# result = grouped['tip_pct', 'total_bill'].agg(functions)
# print(result)
# print(result['tip_pct'])
# 这里也可以传入带有自定义名称的一组元组
# ftuples = [('Durchschnitt', 'mean'),('Abweichung', np.var)]
# print(grouped['tip_pct', 'total_bill'].agg(ftuples))

# 要对一个列或不同的列应用不同的函数。具体的办法是向agg传入一个从列名映射到函数的字典
# # print(grouped.agg({'tip' : np.max, 'size' : 'sum'}))
# print(grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'],
#                    'size' : 'sum'}))
# 以“没有行索引”的形式返回聚合数据
# print(tips.groupby(['day', 'smoker'], as_index=False).mean())

def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]
# print(top(tips, n=6))
# 如果传给apply的函数能够接受其他参数或关键字，则可以将这些内容放在函数名后面一并传入
# print(tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill'))

# 禁止分组键
# print(tips.groupby('smoker', group_keys=False).apply(top))

frame = pd.DataFrame({'data1': np.random.randn(1000),
                      'data2': np.random.randn(1000)})
quartiles = pd.cut(frame.data1, 4)
# print(quartiles[:10])

# def get_stats(group):
#     return {'min': group.min(), 'max':group.max(),
#             'count': group.count(), 'mean': group.mean()}
# grouped = frame.data2.groupby(quartiles)
# # print(grouped.apply(get_stats).unstack())
# grouping = pd.qcut(frame.data1, 10, labels=False)
# grouped = frame.data2.groupby(grouping)
# print(grouped.apply(get_stats).unstack())

states = ['Ohio', 'New York', 'Vermont', 'Florida',
          'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)
# print(data)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
# print(data.groupby(group_key).mean())
# 用分组平均值去填充NA值
# fill_mean = lambda g:g.fillna(g.mean())
# print(data.groupby(group_key).apply(fill_mean))

# 也可以在代码中预定义各组的填充值。由于分组具有一个name属性，所以我们可以拿来用一下
# fill_values = {'East': 0.5, 'West':-1}
# fill_func = lambda g:g.fillna(fill_values[g.name])
# print(data.groupby(group_key).apply(fill_func))

# 随机采样和排列
# Hearts(红桃), Spades(黑桃), Clubs(梅花), Diamonds(方块)
suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10]*3) * 4
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
cards = []
# for suit in suits:
#     cards.extend(str(num) + suit for num in base_names)
# deck = pd.Series(card_val, index=cards)
# # print(deck[:13])
#
# def draw(deck, n=5):
#     return deck.sample(n)
# # print(draw(deck))
#
# get_suit = lambda card: card[-1]
# print(deck.groupby(get_suit).apply(draw, n=2))
# print(deck.groupby(get_suit, group_keys=False).apply(draw, n=2))

df = pd.DataFrame({'category': ['a', 'a', 'a', 'a',
                                'b', 'b', 'b', 'b'],
                   'data': np.random.randn(8),
                   'weights': np.random.rand(8)})
# print(df)
# grouped = df.groupby('category')
# get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
# print(grouped.apply(get_wavg))

def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params

# pt1 = tips.pivot_table(index=['day', 'smoker'])
# print(pt1)

# pt2 = tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker')
# print(pt2)
#
# print('\033[31m控制台显示红色字体\033[0m')
# 传入margins=True添加分项小计。这将会添加标签为All的行和列，其值对应于单个等级中所有数据的分组统计
# pt3 = tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker', margins=True)
# print(pt3)
# pt4 = tips.pivot_table('tip_pct', index=['time', 'size', 'smoker'], columns='day', aggfunc='mean', fill_value=0)
# print(pt4)

# 交叉表（cross-tabulation，简称crosstab）是一种用于计算分组频率的特殊透视表
# ct = pd.crosstab([tips.time, tips.day], tips.smoker, margins=True)
# print(ct)
#
# pt5 = tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker', margins=True)
# print(pt5)
