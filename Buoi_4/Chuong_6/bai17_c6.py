from collections import deque

def position_to_coordinates(pos):
    #Chuyển đổi vị trí từ dạng 'xy' sang tọa độ (x, y).
    column = ord(pos[0]) - ord('a')  # Chuyển đổi từ 'a'-'h' thành 0-7
    row = int(pos[1]) - 1  # Chuyển đổi từ '1'-'8' thành 0-7
    return row, column

def bfs(start, end):
    #Tìm số bước di chuyển tối thiểu từ start đến end.
    # Các hướng di chuyển của quân mã
    directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    queue = deque([(start[0], start[1], 0)])  # (hàng, cột, số bước)
    visited = set()  # Để theo dõi các ô đã đi qua
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()
        
        # Nếu đã đến vị trí đích
        if (x, y) == end:
            return steps
        
        # Thử tất cả các hướng di chuyển
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Kiểm tra nếu vị trí mới nằm trong bàn cờ
            if 0 <= new_x < 8 and 0 <= new_y < 8 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))
    
    return -1  # Nếu không tìm thấy đường đi

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: "))
    
    for _ in range(T):
        ST, EN = input("Nhập vị trí quân mã (ST EN): ").split()
        start = position_to_coordinates(ST)
        end = position_to_coordinates(EN)
        
        # Tìm số bước tối thiểu
        result = bfs(start, end)
        print(result)