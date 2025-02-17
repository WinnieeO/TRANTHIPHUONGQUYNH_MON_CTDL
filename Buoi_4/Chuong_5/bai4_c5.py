def generate(s, index, open_count, close_count, current, results):
    if index == len(s):
        if open_count == close_count:
            results.add(current)
        return
    
    if s[index] == '(':
        generate(s, index + 1, open_count + 1, close_count, current + '(', results)  # Thêm '('
        generate(s, index + 1, open_count, close_count, current, results)  # Bỏ qua '('
    elif s[index] == ')':
        if close_count < open_count:
            generate(s, index + 1, open_count, close_count + 1, current + ')', results)  # Thêm ')'
        generate(s, index + 1, open_count, close_count, current, results)  # Bỏ qua ')'
    else:
        generate(s, index + 1, open_count, close_count, current + s[index], results)  # Thêm ký tự khác

if __name__ == "__main__":
    expression = input("Nhập biểu thức: ").strip()
    results = set()  # Sử dụng tập hợp để lưu trữ kết quả duy nhất
    generate(expression, 0, 0, 0, "", results)
    
    for res in sorted(results):  # Sắp xếp kết quả trước khi in
        print(res)