def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                cost = 0 if s[i-1] == t[j-1] else 1
                dp[i][j] = min(dp[i-1][j] + 1,  # Xóa
                               dp[i][j-1] + 1,  # Chèn
                               dp[i-1][j-1] + cost)  # Thay thế
    return dp[m][n]

# Nhập hai chuỗi từ người dùng
s = input("Nhập chuỗi thứ nhất: ")
t = input("Nhập chuỗi thứ hai: ")

# Tính và hiển thị khoảng cách Levenshtein
print(f"Khoảng cách Levenshtein giữa '{s}' và '{t}' là: {levenshtein_distance(s, t)}")