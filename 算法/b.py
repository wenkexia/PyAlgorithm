from itertools import zip_longest

m, n = map(int, input().split())
a = list(map(int, input().split()))[::-1]
b = list(map(int, input().split()))[::-1]

# a=[9,9,9,9,9][::-1]
# b=[9,9,9,9,9][::-1]
i = 2
res = []
j=0
for s in zip_longest(a,b,fillvalue=0):
    j,k=divmod(s[0] + s[1] + j, i)
    i+=1
    res.append(k)

if j!=0:
    res.append(j)
for i in res[::-1]:
    print(i,end=' ')
