import numpy as np
import pandas as pd
from scipy import stats


# numpy产生随机数讲解 https://blog.csdn.net/jinxiaonian11/article/details/53143141
# 统计函数库scipy.stats的用法 https://blog.csdn.net/u011702002/article/details/78245804

def main():
    rs = np.random.RandomState(24)  # 它是一个容器，用来存储采用梅森旋转产生伪随机数的算法
    n = 20
    t = 10

    # linspace用于创建一个是等差数列的一维数组。它创建的数组元素的数据格式是浮点型。
    # 常看到的一般是三个参数，分别是：起始值、终止值（默认包含自身）、数列个数
    # 另外有一个参数endpoint，用于决定是否包含终止值，如果不设置这个参数，默认为是True
    x = np.linspace(0, t, 100)
    # stats.norm.pdf 正态分布概率密度函数
    # stats.gamma.pdf gam分布概率密度函数
    s = np.array([stats.gamma.pdf(x, a) for a in [3, 5, 7]])
    # print(stats.norm.pdf(0,loc = 0,scale = 1))
    # print(stats.gamma.pdf(10, 3))
    # print(s)

    # numpy中包含的newaxis可以给原数组增加一个维度
    # np.newaxis放的位置不同，产生的新数组也不同
    d = s[:, np.newaxis, :]
    # print(d)

    # numpy.random.RandomState.binomial(n, p, size=None)
    # 表示对一个二项分布进行采样（size表示采样的次数，draw samples from a binomial distribution.），
    # 参数中的n,p分别对应于公式中的n,p，函数的返回值表示n中成功（success）的次数（也即N）
    d = d * np.array([1, -1])[rs.binomial(1, .3, 3)][:, np.newaxis, np.newaxis]
    # np.random.normal(size,loc,scale): 给出均值为loc，标准差为scale的高斯随机数（场）,正态分布
    # loc：float 此概率分布的均值（对应着整个分布的中心centre）
    # scale：float 此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
    # size：int or tuple of ints 输出的shape，默认为None，只输出一个值
    d = d + rs.normal(0, .15, (3, n))[:, :, np.newaxis]
    # numpy.random.uniform(low,high,size)
    # 功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
    # 参数介绍:
    #     low: 采样下界，float类型，默认值为0；
    #     high: 采样上界，float类型，默认值为1；
    #     size: 输出样本数目，为int或元组(tuple)类型，例如，size=(m,n,k), 则输出m*n*k个样本，缺省时输出1个值。
    # 返回值：ndarray类型，其形状和参数size中描述一致。
    d = d + rs.uniform(0, .25, 3)[:, np.newaxis, np.newaxis]
    d *= 10
    # print(d)
    # print(d.shape) # 看形状，说明这是一个a*b*c的数组（矩阵），返回的是一个元组，可以对元组进行索引，也就是0,1,2
    d = d.transpose((1, 2, 0))  # 对数组进行转置
    # print(d.shape)

    # 下面的意思自己对照着csv表格查看
    p = pd.Panel(d,
                 items=pd.Series(np.arange(n), name="subject"),
                 major_axis=pd.Series(x, name="timepoint"),
                 minor_axis=pd.Series(["IPS", "AG", "V1"], name="ROI"),
                 )

    df = p.to_frame().stack().reset_index(name="BOLD signal")
    print(df)
    # df.to_csv("gammas.csv", index=False)


if __name__ == "__main__":
    main()
