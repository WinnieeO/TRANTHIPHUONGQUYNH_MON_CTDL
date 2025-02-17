def longest_valid_substring(s):
    stack = []
    stack.append(-1)
    max_len = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)

    return max_len

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        s = input("Nhập chuỗi: ").strip()
        print(longest_valid_substring(s))