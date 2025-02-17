from collections import deque

def is_prime(num):
    # Kiểm tra xem một số có phải là số nguyên tố hay không
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes():
    # Tạo danh sách các số nguyên tố 4 chữ số.
    primes = []
    for num in range(1000, 10000):
        if is_prime(num):
            primes.append(num)
    return set(primes)

def bfs(start, target, primes):
    # Tìm số bước dịch chuyển tối thiểu từ start đến target.
    queue = deque([(start, 0)])  # (số hiện tại, số bước)
    visited = set()  # Để theo dõi các số đã được kiểm tra
    visited.add(start)

    while queue:
        current, steps = queue.popleft()
        
        if current == target:
            return steps
        
        # Thay đổi từng chữ số để tạo số mới
        for i in range(4):
            for digit in '0123456789':
                if digit != str(current)[i]:
                    new_number = int(str(current)[:i] + digit + str(current)[i+1:])
                    if new_number in primes and new_number not in visited:
                        visited.add(new_number)
                        queue.append((new_number, steps + 1))
    
    return -1  # Nếu không tìm thấy đường đi

if __name__ == "__main__":
    primes = generate_primes()  # Tạo danh sách số nguyên tố 4 chữ số
    T = int(input())
    
    for _ in range(T):
        S, T = map(int, input().split())
        result = bfs(S, T, primes)
        print(result)