def count_word(file_path):
    counter = {}

    # Your Code Here
    with open(file_path, 'r') as file:
        for sentence in file.read().split():
            if sentence in counter:
                counter[sentence] += 1
            else:
                counter[sentence] = 1
    # End Code Here

    return counter
file_path = "P1_data.txt"
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])