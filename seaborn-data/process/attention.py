import os

import pandas as pd


# pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)
# frame:要处理的数据集。
# id_vars:不需要被转换的列名。
# value_vars:需要转换的列名，如果剩下的列全部都要转换，就不用写了。
# var_name和value_name是自定义设置对应的列名。
# col_level :如果列是MultiIndex，则使用此级别。
# 不需要被转换的列循环打印，转换的列列名和值在var_name和value_name下依次打印

def main():
    path1 = os.path.abspath('.')  # 获取当前脚本所在的路径
    path2 = os.path.abspath('..')  # 获取当前脚本所在路径的上一级路径
    df = pd.read_csv(path2 + "/raw/attention.csv")
    df = pd.melt(df, ["subidr", "attnr"], var_name="solutions", value_name="score")
    df.solutions = df.solutions.str[-1].astype(int)
    df.columns = ["subject", "attention", "solutions", "score"]
    print(df)
    # df.to_csv("attention.csv")


if __name__ == "__main__":
    main()