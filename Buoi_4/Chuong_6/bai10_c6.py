from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque() # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        self.elements.append(item) # Thêm phần tử vào cuối deque

    def bfs(self, R, C, grid):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Phải, Dưới, Trái, Trên
        days = 0

        # Thêm tất cả cây non vào hàng đợi
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    self.enqueue((i, j))

        # BFS
        while self.elements:
            size = len(self.elements)
            for _ in range(size):
                x, y = self.elements.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # Hạt nảy mầm thành cây non
                        self.enqueue((nx, ny))
            days += 1

        # Kiểm tra xem có hạt nào chưa nảy mầm không
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1

        return days - 1  # Giảm 1 vì ngày cuối cùng không cần thiết

if __name__ == "__main__":
    queue = Queue()
    T = int(input("Nhập số bộ test: "))
    results = []
    
    for _ in range(T):
        R, C = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(R)]
        
        result = queue.bfs(R, C, grid)
        results.append(result)

    for res in results:
        print(res)