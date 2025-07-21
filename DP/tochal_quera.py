def find_pairs(lst):
    global insides
    pairs = []
    length = len(lst)
    for i in range(length):
        counter = 0
        for j in range(i+1, length):
            counter += 1 if lst[i] <= lst[j] else 0
            if lst[i] == lst[j]:
                pairs.append([i, j])
                insides.append(counter)
    return pairs


def calculate(pairs, insides, i):
    global checker, lst
    length = len(pairs)

    counter = 0
    for j in range(i+1, length):
        if pairs[i][0] < pairs[j][0] and pairs[i][1] > pairs[j][1] and lst[pairs[i][0]] <= lst[pairs[j][0]]:
            if checker[j] != -1:
                counter += checker[j]
            else:
                counter += calculate(pairs, insides, j)
    checker[i] = counter + insides[i]
    return counter + insides[i]


input()
lst = list(map(int, input().split(" ")))
cmprs = [-1] + (lst) + [-1]
print(len(cmprs))
insides = []
pairs = find_pairs(cmprs)
checker = [-1 for _ in range(len(pairs))]
lst = cmprs
print(calculate(pairs, insides, 0) - 1)






