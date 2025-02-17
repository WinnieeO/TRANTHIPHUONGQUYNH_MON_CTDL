from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque() # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        self.elements.append(item) # Thêm phần tử vào cuối deque
    
    def min_operations(self, S, T):
        # Nếu S >= T, chỉ cần thực hiện thao tác (a)
        if S >= T:
            return S - T  # Chỉ thực hiện thao tác trừ 1

        self.enqueue((S, 0))  # (giá trị hiện tại, số bước)
        visited = set()  # Để theo dõi các giá trị đã khám phá
        visited.add(S)

        while self.elements:
            current, steps = self.elements.popleft()

            # Thực hiện thao tác (b): Nhân 2
            next_b = current * 2
            if next_b == T:
                return steps + 1
            if next_b < 10000 and next_b not in visited:
                visited.add(next_b)
                self.enqueue((next_b, steps + 1))

            # Thực hiện thao tác (a): Trừ 1
            next_a = current - 1
            if next_a == T:
                return steps + 1
            if next_a > 0 and next_a not in visited:
                visited.add(next_a)
                self.enqueue((next_a, steps + 1))

        return -1  # Nếu không tìm thấy (không nên xảy ra trong bài toán này)
    
    def display(self):
        print(list(self.elements)) # In hàng đợi từ đầu đến cuối

# Minh họa sử dụng hàng đợi
if __name__ == "__main__":
    queue = Queue()
    Test = 0
    while Test < 1 or Test > 100:
        Test = int(input("Nhập số lượng bộ test (Test <= 100): "))

    for _ in range(Test):
        S = 10001
        T = 10001
        while S >= 10000:
            S = int(input("Nhập S (S < 10000): "))
        while T >= 10000:
            T = int(input("Nhập T (T < 10000): "))
        result = queue.min_operations(S, T)
        print(f"Số lần thực hiện thao tác để chuyển {S} thành {T} là: {result}")