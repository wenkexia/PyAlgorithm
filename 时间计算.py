#从datetime模块导入datetime类和timedelta类
from datetime import datetime, timedelta


start = datetime(2022, 1, 1)
dele = timedelta(1)
ti = 0
while start.year != 2023:
    if start.weekday() in (5, 6) or start.day in (1, 11, 21, 31):
        ti += 1
    start += dele
print(ti)

n = int(input())
list_time = [input().split() for i in range(n)]
last_time = ''
ans = 0
for index_i, i in enumerate(list_time):
    t1, t2, t3 = i[0].split(":")
    t1, t2, t3 = int(t1), int(t2), int(t3)
    if index_i == 0:
        time_1 = datetime(2022, 11, 12, t1, t2, t3)
    else:
        time_2 = datetime(2022, 11, 12, t1, t2, t3)
        ans += (time_2 - time_1).seconds * int(i[1]) * int(i[2])
        last_time = time_2
        print(time_2)
print(ans)