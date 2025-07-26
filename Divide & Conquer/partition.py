# 1:10:19
n = int(input())
lst = list(map(int, input().split(" ")))
def generate(lst):
    i = 0
    new = []
    try:
        while True:
            new += [max(lst[i], lst[i + 1]), lst[i + 1]+lst[i]]
            i += 2
    except IndexError:
        pass
    return new

def step(lst):
    i = 0
    new = []
    try:
        while True:
            new += [max(lst[i], lst[i + 2]), max(lst[i]+lst[i+3], lst[i+1]+lst[i+2])]
            i += 4
    except IndexError:
        pass

    return new
lst = generate(lst)
for i in range(n-1):
    lst = step(lst)
print(max(lst))

