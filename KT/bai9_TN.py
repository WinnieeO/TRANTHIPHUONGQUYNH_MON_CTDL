def my_function(n):
    # Your code here
    max = 0
    for i in n:
        if max < i:
            max = i
    return max

my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))