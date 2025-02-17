def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def apply_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b  # Sử dụng phép chia nguyên

def evaluate_infix(s):
    values = []
    ops = []
    i = 0
    
    while i < len(s):
        if s[i].isdigit():
            val = 0
            while i < len(s) and s[i].isdigit():
                val = (val * 10) + int(s[i])
                i += 1
            values.append(val)
            continue  # Tiếp tục với vòng lặp
        elif s[i] == '(':
            ops.append(s[i])
        elif s[i] == ')':
            while ops and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_op(val1, val2, op))
            ops.pop()  # Loại bỏ dấu mở ngoặc
        else:
            while ops and precedence(ops[-1]) >= precedence(s[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_op(val1, val2, op))
            ops.append(s[i])
        i += 1

    while ops:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(apply_op(val1, val2, op))
    
    return values[-1]

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        expr = input("Nhập biểu thức: ").strip()
        print(evaluate_infix(expr))