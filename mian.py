#
# for i in range(n)；
#     c = list(map(int, input().split()))
#
list1=[]#列表用来存放键盘输入的数据
r=5
for i in range(0,r):#二维列表输入实例
    list1.append(input().split())

print(list1)

# for _ in range(n):
#     pass
#     a, d = input().split()
#     ls += [[int(float(a)), int(float(d))]]

#过滤出列表中的所有奇数
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# reduce() 函数会对参数序列中元素进行累积。
from functools import reduce

def add(x, y) :            # 两数相加
    return x + y
sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数

zip()
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
zip_longest()
