from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque() # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        self.elements.append(item) # Thêm phần tử vào cuối deque

    def min_operations(self, N):
        self.enqueue((N, 0))  # (giá trị hiện tại, số bước)
        visited = set()  # Để theo dõi các giá trị đã khám phá
        visited.add(N)

        while self.elements:
            current, steps = self.elements.popleft()

            # Nếu đã đến 1, trả về số bước
            if current == 1:
                return steps

            # Thao tác (a): Trừ 1
            next_a = current - 1
            if next_a not in visited:
                visited.add(next_a)
                self.enqueue((next_a, steps + 1))

            # Thao tác (b): Tìm các yếu tố
            for i in range(2, int(current**0.5) + 1):
                if current % i == 0:
                    u = i
                    v = current // i
                    max_value = max(u, v)
                    if max_value not in visited:
                        visited.add(max_value)
                        self.enqueue((max_value, steps + 1))

        return -1  # Không nên xảy ra trong bài toán này
        
    def display(self):
        print(list(self.elements)) # In hàng đợi từ đầu đến cuối
        
# Ví dụ sử dụng
if __name__ == "__main__":
    queue = Queue()
    Test = 0
    while Test < 1 or Test > 100:
        Test = int(input("Nhập số lượng bộ test (Test <= 100): "))

    for _ in range(Test):
        N = int(input("Nhập N (N < 10^9): "))
        result = queue.min_operations(N)
        print(f"Số thao tác tối thiểu để biến đổi {N} thành 1 là: {result}")