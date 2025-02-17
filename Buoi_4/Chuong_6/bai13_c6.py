from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()  # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        self.elements.append(item)  # Thêm phần tử vào cuối deque

    def generate_lucky_numbers(self, n):
        # Tạo ra tất cả các số lộc phát có không quá n chữ số.
        lucky_numbers = []
        
        # Tạo số từ 1 đến n chữ số
        for length in range(1, n + 1):
            # Sử dụng phép sinh nhị phân để tạo các tổ hợp
            for i in range(2 ** length):
                number = ''
                for j in range(length):
                    if (i >> j) & 1:
                        number = '8' + number  # Thêm 8 vào đầu
                    else:
                        number = '6' + number  # Thêm 6 vào đầu
                lucky_numbers.append(number)
        
        return lucky_numbers

if __name__ == "__main__":
    queue = Queue()  # Tạo một đối tượng Queue
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        lucky_numbers = queue.generate_lucky_numbers(N)  # Gọi phương thức trong lớp
        
        # Sắp xếp theo thứ tự tăng dần, chuyển sang số nguyên để so sánh
        lucky_numbers.sort(key=lambda x: int(x))
        
        # In số lượng số lộc phát
        print(len(lucky_numbers))
        # In ra kết quả trên một dòng
        print(" ".join(lucky_numbers))