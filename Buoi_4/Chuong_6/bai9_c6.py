from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque() # Sử dụng deque để lưu trữ các phần tử

    def enqueue(self, item):
        self.elements.append(item) # Thêm phần tử vào cuối deque

    def bfs(self, grid, start, end, n):
        # Tìm số bước ít nhất từ start đến end trên bảng grid.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Phải, Dưới, Trái, Trên
        self.enqueue(start)
        visited = set()
        visited.add(start)
        steps = 0

        while self.elements:
            for _ in range(len(self.elements)):
                x, y = self.elements.popleft()
                if (x, y) == end:
                    return steps
                
                # Duyệt các hướng
                for dx, dy in directions:
                    nx, ny = x, y
                    # Tiến tới hướng mới cho đến khi gặp vật cản hoặc ra ngoài bảng
                    while 0 <= nx + dx < n and 0 <= ny + dy < n and grid[nx + dx][ny + dy] != 'X':
                        nx += dx
                        ny += dy
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            self.enqueue((nx, ny))
            
            steps += 1
        
        return -1  # Nếu không tìm thấy đường đi

if __name__ == "__main__":
    queue = Queue()
    T = int(input("Nhập số bộ test: "))
    results = []
    
    for _ in range(T):
        N = int(input())
        grid = [input().strip() for _ in range(N)]
        a, b, c, d = map(int, input().split())
        
        start = (a, b)
        end = (c, d)
        
        result = queue.bfs(grid, start, end, N)
        results.append(result)

    for res in results:
        print(res)