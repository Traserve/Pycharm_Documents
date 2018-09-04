# 基础导入
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# tips = sns.load_dataset("tips") # 库自带
tips = pd.read_csv('seaborn-data\\tips.csv')  # 加载本地csv文件
tips['tip_pct'] = tips['tip']/(tips['total_bill'] - tips['tip'])

# FacetGrid介绍参照picture0，与lmplot对比参照picture6
#
# g = sns.FacetGrid(tips, col="sex", hue="smoker")
# g.map(plt.scatter, "total_bill", "tip", alpha=.7)
# g.add_legend();
# g.savefig('pictures\\picture0')

# lmplot(x, y, data,scatter_kws, line_kws）
# scatter_kws和line_kws的官方解释如下：
# scatter为点，line为线。其实就是用字典去限定点和线的各种属性，如例子所示，散点的颜色为灰石色，线条的颜色为印度红，
# 成像效果就是这样点线颜色分离，展现效果很好。大家也可以换上自己想要的图片属性。
#
# sns.lmplot("total_bill", "tip", tips,
#            scatter_kws={"marker": ".", "color": "slategray"},
#            line_kws={"linewidth": 1, "color": "indianred"}).savefig('pictures\\picture1')


# x_estimator : callable that maps vector -> scalar, optional
# Apply this function to each unique value of x and plot the resulting estimate.
# This is useful when x is a discrete variable. If x_ci is not None,
# this estimate will be bootstrapped and a confidence interval will be drawn.
# 大概解释就是：对拥有相同x水平的y值进行映射，如下：
#
# plt.figure()
# sns.lmplot('size', 'tip', tips, x_estimator= np.mean).savefig('pictures\\picture2')


# jitter是个很有意思的参数, 特别是处理靶数据的overlapping过于严重的情况时,
# 通过增加一定程度的噪声(noise)实现数据的区隔化, 这样原始数据是若干点簇 变成一系列密集邻近的点群.
# 另外, 有的人会经常将 rug 与 jitter 结合使用. 这依人吧.对于横轴取离散水平的时候,
# 用x_jitter可以让数据点发生水平的扰动.但扰动的幅度不宜过大。
#
# sns.lmplot('size', 'tip', tips, x_jitter=.15).savefig('pictures\\picture3')


# seaborn还可以做出xkcd风格的图片：
# with plt.xkcd():
#     sns.color_palette('husl', 8)
#     sns.set_context('paper')
#     sns.lmplot(x='total_bill', y='tip', data=tips, ci=65).savefig('pictures\\picture4')

# with plt.xkcd():
#     sns.lmplot('total_bill', 'tip', data=tips, hue='day')
#     plt.xlabel('hue = day')
#     plt.savefig('pictures\\picture5')

# with plt.xkcd():
#     sns.lmplot('total_bill', 'tip', data=tips, col='sex', hue='smoker')
#     plt.xlabel('hue = smoker')
#     plt.savefig('pictures\\picture6')

# order作用对比：
# sns.set_style('dark')
# sns.set_context('talk')
# sns.lmplot('size', 'total_bill', tips, order=2)
# plt.title('# poly order = 2')
# plt.savefig('pictures\\picture7')
# plt.figure()
# sns.lmplot('size', 'total_bill', tips, order=3)
# plt.title('# poly order = 3')
# plt.savefig('pictures\\picture8')


# "k--"是一个线型选项，用于告诉matplotlib绘制黑色虚线图
# fig = plt.figure()
# 图像应该是2×2的（即最多4张图），且当前选中的是4个subplot中的第一个（编号从1开始）
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# plt.plot(np.random.randn(50).cumsum(), 'k--')
# ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
#
# rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
# circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
# pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)
#
# ax3.add_patch(rect)
# ax3.add_patch(circ)
# ax3.add_patch(pgon)

# 根据日期和聚会规模创建一张交叉表
# party_counts = pd.crosstab(tips['day'], tips['size'])
# print(party_counts)
# party_counts = party_counts.loc[:, 2:5]
# # 进行规格化，使得各行的和为1
# party_pcts = party_counts.div(party_counts.sum(1), axis = 0)
# print(party_pcts)
# 柱状图会将每一行的值分为一组，并排显示
# party_pcts.plot.bar()
# plt.savefig('pictures\\picture9')
# 为DataFrame生成堆积柱状图，这样每行的值就会被堆积在一起
# party_pcts.plot.barh(stacked=True, alpha=0.5)
# plt.savefig('pictures\\picture10')

# # 柱状图的值是tip_pct的平均值。绘制在柱状图上的黑线代表95%置信区间（可以通过可选参数配置）
# sns.barplot(x='tip_pct', y='day', hue='time', data=tips, orient='h')
# plt.savefig('pictures\\picture11')

# 直方图（histogram）是一种可以对值频率进行离散化显示的柱状图。
# 数据点被拆分到离散的、间隔均匀的面元中，绘制的是各面元中数据点的数量
# tips['tip_pct'].plot.hist(bins=50)
# plt.title('tip_pct histogram')
# plt.savefig('pictures\\picture12')

# 密度图，它是通过计算“可能会产生观测数据的连续概率分布的估计”而产生的。
# 一般的过程是将该分布近似为一组核（即诸如正态分布之类的较为简单的分布）。
# 因此，密度图也被称作KDE（Kernel Density Estimate，核密度估计）图
# tips['tip_pct'].plot.density()
# plt.title('tip_pct density plot')
# plt.savefig('pictures\\picture13')

# seaborn的distplot方法绘制直方图和密度图更加简单，还可以同时画出直方图和连续密度估计图
# sns.distplot(tips['tip_pct'], bins=100, color='k')
# plt.savefig('pictures\\picture14')

# regplot方法，它可以做一个散布图，并加上一条线性回归的线，与lmplot类似
# sns.regplot("total_bill", "tip", tips)
# plt.title('regplot')
# plt.savefig('pictures\\picture15')

# 在探索式数据分析工作中，同时观察一组变量的散布图是很有意义的，这也被称为散布图矩阵（scatter plot matrix）。
# 纯手工创建这样的图表很费工夫，所以seaborn提供了一个便捷的pairplot函数，它支持在对角线上放置每个变量的直方图或密度估计
# sns.pairplot(tips, diag_kind='kde', plot_kws={'alpha':0.2})
# plt.title('scatter plot matrix')
# plt.savefig('pictures\\picture16')

# 分面网格facet grid，参照示例1
# sns.factorplot(x='day', y='tip_pct', hue='time', col='smoker',
#                kind='bar', data=tips[tips.tip_pct < 1])
# plt.title('facet grid')
# plt.savefig('pictures\\picture17')

# 除了在分面中用不同的颜色按时间分组，我们还可以通过给每个时间值添加一行来扩展分面网格
# sns.factorplot(x='day', y='tip_pct', row='time',col='smoker',
#                kind='bar', data=tips[tips.tip_pct < 1])

# factorplot支持其它的绘图类型，你可能会用到。例如，盒图（它可以显示中位数，四分位数，和异常值）
# sns.factorplot(x='tip_pct', y='day', kind='box', data=tips[tips.tip_pct < 0.5])
# plt.savefig('pictures\\picture18')


plt.show()