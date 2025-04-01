def max_kernel(num_list, k):
    result = []

    # Your Code Here
    start_index = list(range(0, len(num_list) - k + 1))
    end_index = list(range(k, len(num_list) + 1))
    result = []
    for start_index, end_index in zip(start_index, end_index):
        sub_list= num_list[start_index:end_index]
        result.append(max(sub_list))
    # End Code Here

    return result

assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))