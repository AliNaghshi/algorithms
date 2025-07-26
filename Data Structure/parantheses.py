# 9:42:32
stack = []
string = input()
counter = 1
out = []
fl = 1
for i in string:
    if i == "(":
        stack.append(counter)
    else:
        if stack:
            a = stack.pop()
            out.append([a, counter])
        else:
            fl = 0
            break
    counter += 1
if fl == 1 and not stack:
    for i in out:
        print(i[0], i[1])
else:
    print(-1)

