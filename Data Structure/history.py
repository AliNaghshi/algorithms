# 29:57:25
def insert(i, x):
    global string
    i -= 1
    string = string[:i] + x + string[i:]

def delete(i):
    global string
    i -= 1
    string = string[:i] + string[i+1:]

stack = []
n = int(input())
string = ""


for i in range(n):
    inp = input()
    lst = inp.split(" ")
    kind = lst[0]
    if kind == "undo" and stack:
        stack.pop()
    else:
        stack.append(lst)

for i in stack:
    if i[0] == "insert":
        insert(int(i[1]), i[2])
    else:
        delete(int(i[1]))
print(string)