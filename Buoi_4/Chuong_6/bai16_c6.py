from collections import deque

def bfs(matrix, M, N):
    queue = deque([(0, 0, 0)])  # (hàng, cột, số bước)
    visited = set((0, 0))  # Để theo dõi các ô đã đi qua

    while queue:
        x, y, steps = queue.popleft()
        
        # Nếu đã đến vị trí đích
        if x == M - 1 and y == N - 1:
            return steps
        
        # Tính toán các vị trí mới
        jump_right = y + matrix[x][y]
        jump_down = x + matrix[x][y]
        
        # Đi đến A[i][j + A[i][j]] (kiểm tra vị trí bên phải)
        if jump_right < N and (x, jump_right) not in visited:
            visited.add((x, jump_right))
            queue.append((x, jump_right, steps + 1))
        
        # Đi đến A[i + A[i][j]][j] (kiểm tra vị trí bên dưới)
        if jump_down < M and (jump_down, y) not in visited:
            visited.add((jump_down, y))
            queue.append((jump_down, y, steps + 1))
    
    return -1  # Không tìm thấy đường đi

if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        # Đọc kích thước ma trận
        M, N = map(int, input().split())
        # Đọc ma trận
        matrix = []
        
        # Chia các phần tử vào ma trận
        for i in range(M):
            row = list(map(int, input().split()))
            matrix.append(row)
        
        # Tìm số bước tối thiểu
        result = bfs(matrix, M, N)
        print(result)