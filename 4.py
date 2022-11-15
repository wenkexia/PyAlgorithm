import collections
import time


n = list(input()) * 2

le_n = len(n) // 2
list_ans = collections.defaultdict(list)
ans = ''
le_ans = 0


def re_ans(ans):
    global list_ans, le_ans
    re_ans = ''
    for inex, i in enumerate(ans, 1):
        re_ans += i
        if re_ans not in list_ans[inex]:
            list_ans[inex].append(re_ans)

            le_ans += 1

log = time.time()
count = 1
for index, i in enumerate(n, 1):   #n是字符串数组
    if le_ans < le_n:
        ans += i
        le_ans += 1
        if ans not in list_ans[index]:   #list_ans存入子字符串
            list_ans[index].append(ans)
    elif count < le_n:
        ans = ans[1::] + i

        re_ans(ans)
        count += 1
    else:
        break

print(le_ans)
print(list_ans)
print(time.time() - log)

