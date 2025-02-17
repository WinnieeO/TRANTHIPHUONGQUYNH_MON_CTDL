def evaluate_postfix(s):
    stack = []
    
    for c in s:
        if c.isdigit():  # Kiểm tra nếu c là chữ số
            stack.append(int(c))  # Đẩy chữ số vào ngăn xếp
        else:
            op2 = stack.pop()  # Lấy toán hạng thứ hai
            op1 = stack.pop()  # Lấy toán hạng thứ nhất
            if c == '+':
                stack.append(op1 + op2)
            elif c == '-':
                stack.append(op1 - op2)
            elif c == '*':
                stack.append(op1 * op2)
            elif c == '/':
                stack.append(op1 // op2)  # Sử dụng phép chia nguyên

    return stack[-1]  # Trả về kết quả cuối cùng

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        expr = input("Nhập biểu thức: ").strip()
        print(evaluate_postfix(expr))