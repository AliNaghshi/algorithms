# 5:35:52
n = int(input())
pointer = 0
string = ""
for i in range(n):
    inp = input()
    if "insert" in inp:
        char = inp[-1]
        string = string[:pointer] + char + string[pointer:]
        pointer += 1
    else:
        pointer += 1 if inp == "+" else -1
        pointer = 0 if pointer < 0 else pointer
        pointer = (len(string)-1) if pointer >= len(string) else pointer

print(string)

