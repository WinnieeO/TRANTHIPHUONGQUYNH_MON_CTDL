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
    for _ in range(T):
        expr = input("Nhập biểu thức: ").strip()
        print(to_infix(expr))