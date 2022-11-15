# n = int(float(input()))
n = 5
ls = [
    [1, 5],
    [2, 4],
    [3, 3],
    [4, 2],
    [5, 1]
]
# for _ in range(n):
#     pass
#     a, d = input().split()
#     ls += [[int(float(a)), int(float(d))]]

for j in range(n):
    min_num = float("inf")
    for i in range(n):
        ai, di = ls[i]
        aj, dj = ls[j]
        result = (ai + aj) ** 2 + di + dj
        if result < min_num:
            min_num = result
    print(min_num, end=" ")

print("\b", end="")
print('')
###=======================================>>>
num = [float("inf"), float("inf")]  # [ai**2+bi,ai]
for a, b in ls:
    num = num if num[0] <= a ** 2 + b and a > num[1] else [a ** 2 + b, a]
    print(num[0] + a ** 2 + b + 2 * a * num[1], end=' ')
