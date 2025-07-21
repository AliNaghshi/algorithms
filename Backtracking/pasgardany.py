n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split(" "))))

answerList = []
def choose(lst, j, choosen):
    global answerList
    if j == len(lst):
        srt = sorted(choosen)
        if srt not in answerList:
            answerList.append(srt[:])
        return None
    for i in lst[j]:
        if i not in choosen:
            choosen.append(i)
            choose(lst, j+1, choosen)
            choosen.pop()
    return None
choosen = []
choose(lst, 0, choosen)
print(answerList)
print(len(answerList))


