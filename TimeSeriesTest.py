from datetime import datetime

import numpy as np
import pandas as pd

# 时间序列(time series)数据的意义取决于具体的应用场景，主要有以下几种：
# 1.时间戳（timestamp），特定的时刻。
# 2.固定时期（period），如2007年1月或2010年全年。
# 3.时间间隔（interval），由起始和结束时间戳表示。时期（period）可以被看做间隔（interval）的特例。
# 4.实验或过程时间，每个时间点都是相对于特定起始时间的一个度量。例如，从放入烤箱时起，每秒钟饼干的直径


# now = datetime.now()
# print(now)
# print(now.year, now.month, now.day)

# datetime以毫秒形式存储日期和时间。timedelta表示两个datetime对象之间的时间差
# delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
# print(delta)
# print(delta.days, delta.seconds)

# 可以给datetime对象加上（或减去）一个或多个timedelta，这样会产生一个新对象
# start = datetime(2011, 1, 7)
# print(start + timedelta(12))
# print(start - 2 * timedelta(12))

# 利用str或strftime方法（传入一个格式化字符串），datetime对象和pandas的Timestamp对象（稍后就会介绍）可以被格式化为字符串
# stamp = datetime(2011, 1, 3)
# print(str(stamp))
# print(stamp.strftime('%Y-%m-%d'))

# datetime.strptime可以用这些格式化编码将字符串转换为日期
# value = '2011-01-03'
# print(datetime.strptime(value, '%Y-%m-%d'))
# datestrs = ['7/6/2011', '8/6/2011']
# print([datetime.strptime(x, '%m/%d/%Y') for x in datestrs])

# # 每次都要编写格式定义是很麻烦的事情，尤其是对于一些常见的日期格式。这种情况下，你可以用dateutil这个第三方包中的parser.parse方法
# print(parse('2011-01-03'))
# print(parse('Jan 31, 1997 10:45 PM'))
# # 在国际通用的格式中，日出现在月的前面很普遍，传入dayfirst=True即可解决这个问题
# print(parse('6/12/2011', dayfirst=True))

# pandas通常是用于处理成组日期的，不管这些日期是DataFrame的轴索引还是列。to_datetime方法可以解析多种不同的日期表示形式。对标准日期格式（如ISO8601）的解析非常快
# datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
# print(pd.to_datetime(datestrs))
# # 它还可以处理缺失值（None、空字符串等）
# idx = pd.to_datetime(datestrs + [None])
# print(idx)
# print(pd.isnull(idx))

# pandas最基本的时间序列类型就是以时间戳（通常以Python字符串或datatime对象表示）为索引的Series
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)
# print(ts)
# print(ts.index)
# print(ts[::2]) # ts[::2] 是每隔两个取一个

# pandas用NumPy的datetime64数据类型以纳秒形式存储时间戳
# print(ts.index.dtype)
# DatetimeIndex中的各个标量值是pandas的Timestamp对象
# stamp = ts.index[2]
# print(stamp)
# 当你根据标签索引选取数据时，时间序列和其它的pandas.Series很像
# print(ts[stamp])
# 还有一种更为方便的用法：传入一个可以被解释为日期的字符串
# print(ts['1/10/2011'])
# print(ts['20110110'])

# 对于较长的时间序列，只需传入“年”或“年月”即可轻松选取数据的切片
# longer_ts = pd.Series(np.random.randn(1000),
#                       index=pd.date_range('1/1/2000', periods=1000))
# print(longer_ts)
# print(longer_ts['2001'])
# print(longer_ts['2001-05'])
# print(ts[datetime(2011, 1, 7):])
# print(ts['1/6/2011':'1/11/2011'])
# print(ts.truncate(after='1/9/2011'))
# 这样切片所产生的是原时间序列的视图，跟NumPy数组的切片运算是一样的。
# 这意味着，没有数据被复制，对切片进行修改会反映到原始数据上。

# 面这些操作对DataFrame也有效。例如，对DataFrame的行进行索引
# dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
# long_df = pd.DataFrame(np.random.randn(100, 4), index=dates,
#                        columns=['Colorado', 'Texas', 'New York', 'Ohio'])
# print(long_df.loc['5-2001'])


# 带有重复索引的时间序列
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000',
                          '1/2/2000', '1/3/2000'])
dup_ts = pd.Series(np.arange(5), index=dates)
# print(dup_ts)
# 通过检查索引的is_unique属性，我们就可以知道它是不是唯一的
# print(dup_ts.index.is_unique)

# 对这个时间序列进行索引，要么产生标量值，要么产生切片，具体要看所选的时间点是否重复
# print(dup_ts['1/3/2000']) # 不重复
# print(dup_ts['1/2/2000']) # 重复

# 假设你想要对具有非唯一时间戳的数据进行聚合。一个办法是使用groupby，并传入level=0
# grouped = dup_ts.groupby(level=0)
# print(grouped.mean(), '\n', grouped.count())

# 将之前那个时间序列转换为一个具有固定频率（每日）的时间序列
# print(ts)
# resample = ts.resample('D') # 字符串“D”是每天的意思
# print(resample)

# pandas.date_range可用于根据指定的频率生成指定长度的DatetimeIndex
# index = pd.date_range('2012-04-01', '2012-06-01')
# print(index)
# print(pd.date_range(start='2012-04-01', periods=20))
# print(pd.date_range(end='2012-06-01', periods=20))

# 如果你想要生成一个由每月最后一个工作日组成的日期索引，可以传入"BM"频率（表示business end of month 每月最后一个工作日），
# 这样就只会包含时间间隔内（或刚好在边界上的）符合频率要求的日期
# print(pd.date_range('2018-01-01', '2018-12-01', freq='BM'))

# date_range默认会保留起始和结束时间戳的时间信息（如果有的话）
# print(pd.date_range('2012-05-02 12:56:31', periods=5))
# 有时，虽然起始和结束日期带有时间信息，但你希望产生一组被规范化（normalize）到午夜的时间戳。normalize选项即可实现该功能
# print(pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True))

# 频率和日期偏移量
# pandas中的频率是由一个基础频率（base frequency）和一个乘数组成的。基础频率通常以一个字符串别名表示，
# 比如"M"表示每月，"H"表示每小时。对于每个基础频率，都有一个被称为日期偏移量（date offset）的对象与之对应。
# hour = Hour(4)
# print(hour)

# 一般来说，无需明确创建这样的对象，只需使用诸如"H"或"4H"这样的字符串别名即可。在基础频率前面放上一个整数即可创建倍数：
# print(pd.date_range('2000-01-01', '2000-01-03 23:59', freq='4h'))

# 大部分偏移量对象都可通过加法进行连接
# print(Hour(2) + Minute(30))
# 同理，你也可以传入频率字符串（如"2h30min"），这种字符串可以被高效地解析为等效的表达式
# print(pd.date_range('2000-01-01', periods=10, freq='1h30min'))

# WOM日期
# WOM（Week Of Month）是一种非常实用的频率类，它以WOM开头。它使你能获得诸如“每月第3个星期五”之类的日期
# rng = pd.date_range('2012-01-01', '2012-09-01', freq='WOM-3FRI')
# print(list(rng))

# 移动（超前和滞后）数据
# 移动（shifting）指的是沿着时间轴将数据前移或后移。Series和DataFrame都有一个shift方法用于执行单纯的前移或后移操作，保持索引不变：
