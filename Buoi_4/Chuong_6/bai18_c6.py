from collections import deque

def rotate(state, index):
    # Quay miếng ghép tại chỉ số index theo chiều kim đồng hồ.
    new_state = list(state)
    if index == 0:  # Quay miếng ghép đầu tiên
        new_state[0], new_state[1], new_state[3], new_state[4] = state[3], state[0], state[4], state[1]
    elif index == 1:  # Quay miếng ghép thứ hai
        new_state[1], new_state[0], new_state[2], new_state[5] = state[0], state[1], state[5], state[2]
    elif index == 2:  # Quay miếng ghép thứ ba
        new_state[2], new_state[1], new_state[5], new_state[4] = state[1], state[5], state[4], state[2]
    elif index == 3:  # Quay miếng ghép thứ tư
        new_state[3], new_state[0], new_state[4], new_state[5] = state[0], state[4], state[5], state[3]
    elif index == 4:  # Quay miếng ghép thứ năm
        new_state[4], new_state[3], new_state[5], new_state[2] = state[3], state[5], state[2], state[4]
    elif index == 5:  # Quay miếng ghép thứ sáu
        new_state[5], new_state[4], new_state[2], new_state[1] = state[4], state[2], state[1], state[5]
    return tuple(new_state)

def bfs(start, target):
    # Tìm số phép biến đổi tối thiểu từ trạng thái ban đầu đến trạng thái đích.
    queue = deque([(start, 0)])  # (trạng thái hiện tại, số bước)
    visited = set()  # Để theo dõi các trạng thái đã được kiểm tra
    visited.add(start)

    while queue:
        current_state, steps = queue.popleft()
        
        # Nếu đã đạt đến trạng thái đích
        if current_state == target:
            return steps
        
        # Thử quay từng miếng ghép
        for i in range(6):
            next_state = rotate(current_state, i)
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + 1))
    
    return -1  # Không thể đạt được trạng thái đích

if __name__ == "__main__":
    T = int(input("Nhập số bộ test: "))
    
    for _ in range(T):
        # Đọc trạng thái ban đầu
        start = tuple(map(int, input("Nhập trạng thái ban đầu: ").split()))
        # Đọc trạng thái đích
        target = tuple(map(int, input("Nhập trạng thái đích: ").split()))
        
        # Tìm số phép biến đổi tối thiểu
        result = bfs(start, target)
        print(result)