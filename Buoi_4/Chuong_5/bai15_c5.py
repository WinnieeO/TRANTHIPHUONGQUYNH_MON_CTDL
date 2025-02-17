def next_smaller_after_greater(A):
    n = len(A)
    ans = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and A[stack[-1]] <= A[i]:
            stack.pop()
        
        if stack:
            greater_index = stack[-1]
            smaller_found = False
            for j in range(greater_index + 1, n):
                if A[j] < A[greater_index]:
                    ans[i] = A[j]
                    smaller_found = True
                    break
            
            if not smaller_found:
                ans[i] = -1
        
        stack.append(i)

    return ans

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        n = int(input("Nhập n: ").strip())
        arr = list(map(int, input("Nhập mảng: ").strip().split()))
        res = next_smaller_after_greater(arr)
        
        print(res)