from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque() # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        self.elements.append(item) # Thêm phần tử vào cuối deque
    
    def find_smallest_multiple_of(self, item):
        self.elements.clear()
        self.enqueue('9')
        while self.elements:
            current = self.elements.popleft()  # Lấy số đầu tiên trong hàng đợi

            # Kiểm tra nếu số hiện tại chia hết cho target
            if int(current) % item == 0:
                return current

            # Thêm các số mới vào hàng đợi
            self.elements.append(current + '0')  # Thêm 0 vào cuối
            self.elements.append(current + '9')  # Thêm 9 vào cuối
    
    def display(self):
        print(list(self.elements)) # In hàng đợi từ đầu đến cuối

# Minh họa sử dụng hàng đợi
if __name__ == "__main__":
    T = 0
    while T < 1 or T > 100:
        T = int(input("Nhập số lượng bộ test (T <= 100): "))

    for _ in range(T):
        n = 0
        while n < 1 or n > 100:
            n = int(input("Nhập số N (N <= 100): "))
        queue = Queue()
        smallest_multiple = queue.find_smallest_multiple_of(n)
        print(f"Số nhỏ nhất chỉ gồm chữ số 0 và 9, chia hết cho {n} là: {smallest_multiple}")