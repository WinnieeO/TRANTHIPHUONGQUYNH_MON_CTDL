def largest_rectangle_area(heights):
    n = len(heights)
    max_area = 0
    stack = []
    left = [-1] * n
    right = [n] * n

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            right[stack.pop()] = i
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    for i in range(n):
        max_area = max(max_area, heights[i] * (right[i] - left[i] - 1))

    return max_area

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        n = int(input("Nhập n: ").strip())
        heights = list(map(int, input("Nhập chiều cao: ").strip().split()))
        print(largest_rectangle_area(heights))