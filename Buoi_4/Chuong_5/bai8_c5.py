def to_postfix(s):
    stack = []
    
    # Duyệt qua chuỗi từ phải sang trái
    for i in range(len(s) - 1, -1, -1):
        if s[i].isalnum():  # Kiểm tra nếu ký tự là alphanumeric
            stack.append(s[i])
        else:
            op1 = stack.pop()  # Lấy toán hạng thứ nhất
            op2 = stack.pop()  # Lấy toán hạng thứ hai
            stack.append(op1 + op2 + s[i])  # Ghép lại theo thứ tự postfix

    return stack[-1]  # Trả về biểu thức postfix cuối cùng

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        expr = input("Nhập biểu thức: ").strip()
        print(to_postfix(expr))