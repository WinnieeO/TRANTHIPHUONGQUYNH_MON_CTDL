def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def to_postfix(s):
    ops = []
    res = ""

    for c in s:
        if c.isalnum():  # Kiểm tra nếu c là ký tự alphanumeric
            res += c
        elif c == '(':
            ops.append(c)
        elif c == ')':
            while ops and ops[-1] != '(':
                res += ops.pop()
            ops.pop()  # Bỏ dấu '(' ra khỏi ngăn xếp
        else:  # c là một toán tử
            while ops and precedence(ops[-1]) >= precedence(c):
                res += ops.pop()
            ops.append(c)

    while ops:
        res += ops.pop()

    return res

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        expr = input("Nhập biểu thức: ").strip()
        print(to_postfix(expr))