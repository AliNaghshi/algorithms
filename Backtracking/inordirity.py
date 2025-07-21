n, k = map(int, input().split(" "))
inordirity = 0


def find_inordirity(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i > j and lst[i] < lst[j]:
                counter += 1
    return counter

def generate_sequence(lst, n):
    global inordirity, k
    if len(lst) > n:
        return None
    if len(lst) == n:
        return lst

    for i in range(1, n+1):
        if i not in lst:
            lst.append(i)
            retLst = generate_sequence(lst, n)
            if retLst:
                if find_inordirity(lst) == k:
                    inordirity += 1
            lst.pop()
    return None

lst = []
generate_sequence(lst, n)
print(inordirity)

