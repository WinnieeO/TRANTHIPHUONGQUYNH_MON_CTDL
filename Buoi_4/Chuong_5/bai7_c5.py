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

def to_infix(s):
    stack = []
    
    for c in s:
        if c.isalnum():  # Kiểm tra nếu c là ký tự alphanumeric
            stack.append(c)
        else:
            op2 = stack.pop()  # Lấy toán hạng thứ hai
            op1 = stack.pop()  # Lấy toán hạng thứ nhất
            stack.append(f"({op1}{c}{op2})")  # Tạo biểu thức infix

    return stack[-1]  # Trả về biểu thức infix cuối cùng

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())

    expressions = []

    for _ in range(T):
        expr = input("Nhập biểu thức: ").strip()
        temp = to_postfix(expr)
        print(to_infix(temp))