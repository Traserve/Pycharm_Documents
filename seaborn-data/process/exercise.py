import os
import pandas as pd

# 值替换，列删除
def main():
    df = pd.read_csv(os.path.abspath('..') + "/raw/exercise.csv")
    df["diet"] = df.diet.map({1: "low fat", 2: "no fat"})
    df["kind"] = df.exertype.map({1: "rest", 2: "walking", 3: "running"})
    df["time"] = df.time.map({1: "1 min", 2: "15 min", 3: "30 min"})
    df = df.drop(["exertype"], axis=1)
    print(df)
    # df.to_csv("exercise.csv")


if __name__ == "__main__":
    main()
