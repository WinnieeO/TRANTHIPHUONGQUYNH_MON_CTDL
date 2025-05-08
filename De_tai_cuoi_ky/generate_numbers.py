import random

# Sinh 100 số ngẫu nhiên từ 1 đến 1000
numbers = [random.randint(1, 1000) for _ in range(100)]

# Ghi vào file txt
with open('data_new.txt', 'w') as file:
    for number in numbers:
        file.write(str(number) + '\n')