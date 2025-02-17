def smallest_number(s):
    n = len(s)
    result = []
    stack = []

    for i in range(n + 1):
        stack.append(str(i + 1))  # Thêm số từ 1 đến n+1 vào ngăn xếp
        if i == n or s[i] == 'I':
            while stack:
                result.append(stack.pop())  # Lấy các số từ ngăn xếp ra khi gặp 'I' hoặc kết thúc chuỗi

    return ''.join(result)

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        s = input("Nhập chuỗi: ").strip()
        print(smallest_number(s))