def normalize(s):
    ops = [True]  # Ngăn xếp để theo dõi trạng thái của các toán tử
    res = ""

    for i in range(len(s)):
        if s[i] == '(':
            if i > 0 and s[i - 1] == '-':
                ops.append(not ops[-1])  # Đảo ngược trạng thái
            else:
                ops.append(ops[-1])  # Giữ nguyên trạng thái
        elif s[i] == ')':
            ops.pop()  # Loại bỏ trạng thái khi gặp dấu đóng
        elif s[i] in '+-':
            if ops[-1]:
                res += s[i]  # Thêm toán tử nếu trạng thái là True
            else:
                res += '-' if s[i] == '+' else '+'  # Đảo ngược toán tử
        else:
            res += s[i]  # Thêm ký tự khác vào kết quả

    return res

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        P1 = input("Nhập biểu thức P1: ").strip()
        P2 = input("Nhập biểu thức P2: ").strip()
        if normalize(P1) == normalize(P2):
            print("YES")
        else:
            print("NO")