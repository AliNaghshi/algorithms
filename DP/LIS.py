def LIS(lst):
    n = len(lst)
    dp = [1 for _ in range(n+1)]
    for i in range(n):
        for j in range(i, n):
            if lst[j]>lst[i]:
                dp[j+1] = max(1+dp[i+1], dp[j])
    return max(dp)


def main():
    lst = list(map(int, input().split(" ")))
    print(LIS(lst))


if __name__ == "__main__":
    main()
