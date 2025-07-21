def generate(word, n):
    if len(word) > n:
        return
    if len(word) == n:
        print(word)
        return
    generate(word + "a",  n)
    generate(word + "b",  n)
    generate(word + "c",  n)


generate("", 3)
