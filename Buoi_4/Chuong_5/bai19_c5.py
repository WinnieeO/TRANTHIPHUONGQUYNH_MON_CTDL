def stock_span(prices):
    n = len(prices)
    span = [1] * n
    stack = []

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span[i] = (i + 1) if not stack else (i - stack[-1])
        stack.append(i)

    return span

if __name__ == "__main__":
    T = int(input("Nhập số lượng test: ").strip())
    for _ in range(T):
        n = int(input("Nhập n: ").strip())
        prices = list(map(int, input("Nhập giá cổ phiếu: ").strip().split()))
        res = stock_span(prices)
        print(" ".join(map(str, res)))