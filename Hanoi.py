# 汉诺塔
def hanoi(n, src, dst, mid):
    global count;
    if n == 1:
        print("{}:{}->{}".format(n, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, mid, dst))
        count +=1
        hanoi(n-1, mid, dst, src)
count = 0;
num = 3
hanoi(num, "A","C","B")
print(count)