from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque() # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        self.elements.append(item) # Thêm phần tử vào cuối deque

    def is_valid_number(self, K):
        # Kiểm tra xem số K có tất cả các chữ số khác nhau và nhỏ hơn hoặc bằng 5 hay không.
        digits = str(K)
        seen = set()
        for digit in digits:
            if digit in seen or int(digit) > 5:
                return False
            seen.add(digit)
        return True

    def count_valid_numbers(self, L, R):
        # Đếm số các số K trong khoảng [L, R] thỏa mãn điều kiện."""
        count = 0
        for K in range(L, R + 1):
            if self.is_valid_number(K):
                count += 1
        return count

if __name__ == "__main__":
    queue = Queue()
    T = int(input("Nhập số lượng test (T ≤ 100): "))
    results = []
    
    for _ in range(T):
        L, R = map(int, input().split())
        result = queue.count_valid_numbers(L, R)
        results.append(result)

    for res in results:
        print(res)