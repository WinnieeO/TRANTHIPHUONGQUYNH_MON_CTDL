def has_redundant_parentheses(exp):
    stack = []

    for ch in exp:
        if ch == ')':
            top = stack.pop()
            is_redundant = True
            
            while stack and top != '(':
                if top in ['+', '-', '*', '/']:
                    is_redundant = False
                top = stack.pop()
            
            if is_redundant:
                return True
        else:
            stack.append(ch)
    
    return False

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: "))
    
    for _ in range(T):
        exp = input("Nhập biểu thức: ")
        
        if has_redundant_parentheses(exp):
            print("Yes")
        else:
            print("No")