class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push (self, value):
        ### Your Code Here
        if not self.is_full():
            self.__stack.append(value)
        ### End Code Here

    def top(self):
        ### Your Code Here
        if len(self.__stack) > 0:  # Kiểm tra stack không rỗng
            return self.__stack[-1]
        return None  # Trả về None nếu stack rỗng
        # End Code Here

stack1 = MyStack(capacity = 5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.top())