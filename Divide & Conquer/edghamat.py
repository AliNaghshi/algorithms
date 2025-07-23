
def merged(l, r):
    lst = []
    x, y = 0, 0
    for _ in range(len(l + r)):
        if x < len(l) and y < len(r):
            if l[x]< r[y]:
                lst.append(l[x])
                x += 1
            else:
                lst.append(r[y])
                y += 1
        else:
            if x == len(l):
                for i in range(y, len(r)):
                    lst.append(r[i])
            else:
                for i in range(x, len(l)):
                    lst.append(l[i])
            break
    return lst

def merge(total, i, j):
    if j == i:
        return total[i]
    if j - i == 1:
        return merged(total[i], total[j])
    mid = (i+j) // 2
    l = merge(total, i, mid)
    r = merge(total, mid+1, j)
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
prt(merge(total, 0, len(total)-1))

