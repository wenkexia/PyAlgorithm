m,n = map(int,input().split())
a= list(map(int,input().split()))
a= sorted(a,reverse=True)
if n == 0:
    print(a[0]-a[m-1])

l= 0
r= n-1
max_n = max(a)
min_n = min(a)

while n>=0:

