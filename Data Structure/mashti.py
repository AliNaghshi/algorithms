import time
dic = {}
def func(a, b):
    global dic
    if (a, b) in dic:
        return dic[(a, b)]
    z = 1
    x = 1
    for i in range(b+1, a+b+1):
        z *= i
        if x <= a:
            z /= x
            x += 1
        z = (int(z)) % 1000000007
    dic[(a, b)] = z
    return z


t, k = map(int, input().split(" "))

lst = []
mini, maxi = float('inf'), 0
for i in range(t):
    a = list(map(int, input().split(" ")))
    lst.append(a)
    mini = min(a[0], mini)
    maxi = max(a[1], maxi)
ps = [0 for _ in range(maxi - mini+2)]
sumer = 0
for i in range(mini, maxi+1):
    counter = 0
    zc, oc = 0, i
    while oc >= 0:
        counter += func(zc, oc)
        oc -= k
        zc += 1
    sumer += counter%1000000007
    ps[i-mini+1] = sumer%1000000007

for i in lst:
    a, b = i
    print(ps[b-mini + 1] - ps[a-mini])

