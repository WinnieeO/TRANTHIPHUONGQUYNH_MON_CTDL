def greater_frequency_right(arr):
    n = len(arr)
    res = [-1] * n
    freq = {}
    stack = []

    # Đếm tần suất của mỗi phần tử
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Tìm phần tử có tần suất lớn hơn bên phải
    for i in range(n):
        while stack and freq[arr[stack[-1]]] < freq[arr[i]]:
            res[stack.pop()] = arr[i]
        stack.append(i)

    return res

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        n = int(input("Nhập n: ").strip())
        arr = list(map(int, input("Nhập mảng: ").strip().split()))
        res = greater_frequency_right(arr)
        print(" ".join(map(str, res)))