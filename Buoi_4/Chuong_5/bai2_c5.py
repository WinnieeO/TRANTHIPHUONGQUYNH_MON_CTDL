def solve(s):
    balance = 0
    changes = 0
    for c in s:
        if c == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            changes += 1
            balance = 1  # Đặt lại balance về 1 vì đã thay đổi

    changes += balance // 2  # Thêm các dấu ngoặc mở còn lại
    return changes

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    results = []
    
    for _ in range(T):
        S = input().strip()  # Đọc chuỗi mà không có khoảng trắng
        results.append(solve(S))
    
    for res in results:
        print(res)