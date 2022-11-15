'''
3.Lucky_number
小于n的素数，不能包含有k这个数字
'''

n, k = 30, 2
# n, k = int(input()),int(input())
num = []
for i in range(2, n + 1):
    tmp = 0
    for j in range(1, i + 1):
        if i % j == 0:
            tmp += 1
        # if tmp >= 2: break
    if tmp == 2 and str(k) not in str(i):
        num.append(i)

print(num)
print(len(num))
