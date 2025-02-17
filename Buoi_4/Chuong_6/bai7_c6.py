from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque() # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        self.elements.append(item) # Thêm phần tử vào cuối deque

    def is_one_char_diff(self, word1, word2):
        # Kiểm tra xem word1 và word2 khác nhau một ký tự hay không.
        diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
        return diff_count == 1

    def shortest_word_transformation(self, S, s, t):
        # Tìm khoảng cách đường đi ngắn nhất từ s đến t.
        if s == t:
            return 0  # Nếu s và t đã giống nhau

        self.enqueue((s, 1))  # Hàng đợi chứa tuple (xâu hiện tại, số bước)
        visited = set([s])  # Tập hợp chứa các xâu đã khám phá

        while self.elements:
            current_word, steps = self.elements.popleft()

            # Duyệt qua tất cả các xâu trong S
            for word in S:
                if word not in visited and self.is_one_char_diff(current_word, word):
                    # Nếu từ mới khác nhau 1 ký tự và chưa được khám phá
                    if word == t:
                        return steps + 1  # Trả về số bước nếu tìm thấy t
                    visited.add(word)  # Đánh dấu từ này là đã khám phá
                    self.enqueue((word, steps + 1))  # Thêm vào hàng đợi

        return -1  # Nếu không tìm thấy đường đi

# Ví dụ sử dụng
if __name__ == "__main__":
    queue = Queue()
    T = int(input("Nhập số lượng test (T ≤ 100): "))
    for _ in range(T):
        # Nhập n, s, t
        n, s, t = input().split()
        n = int(n)  # Chuyển n sang số nguyên

        # Nhập n từ và chia thành danh sách
        S = input().split()

        # Gọi hàm để tính khoảng cách ngắn nhất
        result = queue.shortest_word_transformation(S, s, t)
        print(f"Khoảng cách đường đi ngắn nhất từ '{s}' đến '{t}' là: {result}")