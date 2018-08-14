str = input("请输入字符串：")
print(str[::-1])
def rvs(s):
    print(s)
    if s == "":
        return ""
    else:
        return rvs(s[1:]) + s[0]
print(rvs(str))