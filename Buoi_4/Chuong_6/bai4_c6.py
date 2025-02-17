from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque() # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        self.elements.append(item) # Thêm phần tử vào cuối deque
    
    def count_bdn_less_than_n(self, N):
        self.elements.clear()
        self.enqueue('1')
        while self.elements:
            current = self.elements.popleft()  # Lấy số đầu tiên trong hàng đợi

            # Kiểm tra nếu số hiện tại nhỏ hơn N
            if int(current) % N == 0:
                return current

            # Thêm các số mới vào hàng đợi
            self.elements.append(current + '0')  # Thêm 0 vào cuối
            self.elements.append(current + '1')  # Thêm 9 vào cuối
    
    def display(self):
        print(list(self.elements)) # In hàng đợi từ đầu đến cuối

# Minh họa sử dụng hàng đợi
if __name__ == "__main__":
    queue = Queue()
    T = 0
    while T < 1 or T > 100:
        T = int(input("Nhập số lượng bộ test (T <= 100): "))

    for _ in range(T):
        n = 0
        while n < 1 or n >= 1000:
            n = int(input("Nhập số N ( 0 < N < 1000): "))
        result = queue.count_bdn_less_than_n(n)
        print(f"Số BDN của {n} là: {result}")