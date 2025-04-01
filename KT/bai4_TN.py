def levenshtein_distance(token1, token2):
    # Your Code Here
    m, n = len(token1), len(token2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                cost = 0 if token1[i-1] == token2[j-1] else 1
                dp[i][j] = min(dp[i-1][j] + 1,  # Xóa
                               dp[i][j-1] + 1,  # Chèn
                               dp[i-1][j-1] + cost)  # Thay thế
    distance = dp[i][j]
    # End Code Here

    return distance

assert levenshtein_distance("hi", "hello") == 4.0
print(levenshtein_distance("hola", "hello"))