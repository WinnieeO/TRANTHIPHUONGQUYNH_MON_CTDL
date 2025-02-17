def decode_string(s):
    count_stack = []
    string_stack = []
    current_string = ""
    current_num = 0

    for c in s:
        if c.isdigit():
            current_num = current_num * 10 + int(c)
        elif c == '[':
            count_stack.append(current_num)
            string_stack.append(current_string)
            current_string = ""
            current_num = 0
        elif c == ']':
            temp = current_string
            current_string = string_stack.pop()
            repeat_times = count_stack.pop()
            current_string += temp * repeat_times
        else:
            current_string += c

    return current_string

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        s = input("Nhập chuỗi: ").strip()
        print(decode_string(s))