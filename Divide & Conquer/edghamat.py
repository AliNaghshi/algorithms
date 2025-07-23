
def merged(l, r):
    lst = []
    for i in range(len(l + r)):
        if len(l) and len(r):
            if l[0] < r[0]:
                lst.append(l[0])
                l.pop(0)
            else:
                lst.append(r[0])
                r.pop(0)
        else:

            lst += l + r
    return lst

def merge(total, i, j):
    if j == i:
        return total[i]
    if j - i == 1:
        return merged(total[i], total[j])
    mid = (i+j) // 2
    print(i, j, mid)
    l = merge(total, i, mid)
    r = merge(total, mid+1, j)
    print(l, r)
    return merged(r, l)



def prt(lst):
    for i in lst:
        print(i, end=" ")
    print()


n, k = map(int, input().split(" "))
total = []
for i in range(k):
    lst = list(map(int, input().split(" ")))
    total.append(lst)
print(total)
prt(merge(total, 0, len(total)-1))

