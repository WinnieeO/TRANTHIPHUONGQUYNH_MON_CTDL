def my_function(n):
    # Your code here
    min = 0
    for i in n:
        if min > i:
            min = i
    return min
my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function(my_list))