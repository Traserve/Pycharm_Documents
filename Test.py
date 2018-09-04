import pandas as pd
import numpy as np

a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
# NumPy的where函数，它表示一种等价于面向数组的if-else
print(np.where(pd.isnull(a), b, a))
# Series有一个combine_first方法，实现的也是一样的功能，还带有pandas的数据对齐：
print(b[:-2].combine_first(a[2:]))