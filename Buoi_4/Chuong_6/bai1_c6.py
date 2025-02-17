from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque() # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        self.elements.append(item) # Thêm phần tử vào cuối deque
    
    def clear(self):
        self.elements.clear()  # Xóa tất cả các phần tử trong hàng đợi
    
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
        while n < 1 or n > 10000:
            n = int(input("Nhập số n (n <= 10000): "))
        for i in range(1, n+1):
            queue.enqueue(bin(i)[2:])
        print(f"Số nhị phân từ 1 đến {n} là ")
        queue.display()
        queue.clear()