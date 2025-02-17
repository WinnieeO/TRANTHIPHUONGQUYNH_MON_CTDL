from collections import deque

def bfs(start, end, grid, A, B, C):
    directions = [
        (1, 0, 0), (-1, 0, 0),  # Di chuyển lên/xuống
        (0, 1, 0), (0, -1, 0),  # Di chuyển trái/phải
        (0, 0, 1), (0, 0, -1)   # Di chuyển trước/sau
    ]
    
    queue = deque([start])
    visited = set()
    visited.add(start)
    steps = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            x, y, z = queue.popleft()
            if (x, y, z) == end:
                return steps
            
            for dx, dy, dz in directions:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < A and 0 <= ny < B and 0 <= nz < C and (nx, ny, nz) not in visited:
                    if grid[nx][ny][nz] != '#':
                        visited.add((nx, ny, nz))
                        queue.append((nx, ny, nz))
        
        steps += 1

    return -1  # Không tìm thấy đường đi

if __name__ == "__main__":
    T = int(input("Nhập số bộ test: "))
    results = []
    
    for _ in range(T):
        A, B, C = map(int, input().split())
        grid = []
        
        for a in range(A):
            layer = []
            for b in range(B):
                row = input().strip()
                if len(row) != C:
                    print(f"Lỗi dữ liệu: Dòng {b + 1} trong lớp {a + 1} không đủ {C} ký tự.")
                    exit(1)
                layer.append(row)
            grid.append(layer)
            if a < A - 1:  # Đọc dòng trống giữa các khối
                input()

        start = None
        end = None
        
        # Tìm tọa độ S và E
        for i in range(A):
            for j in range(B):
                for k in range(C):
                    if grid[i][j][k] == 'S':
                        start = (i, j, k)
                    elif grid[i][j][k] == 'E':
                        end = (i, j, k)

        if start is not None and end is not None:
            result = bfs(start, end, grid, A, B, C)
            results.append(result)
        else:
            results.append(-1)  # Không tìm thấy S hoặc E

    for res in results:
        print(res)