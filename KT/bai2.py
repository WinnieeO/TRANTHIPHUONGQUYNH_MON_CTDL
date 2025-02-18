def count_chars(string):
    string = string.lower()
    character_statistic = {}
    for character in string:
        if character in character_statistic:
            character_statistic[character] += 1
        else:
            character_statistic[character] = 1

    print(character_statistic)

if __name__ == "__main__":
    s = input("Nhập một từ: ")
    count_chars(s)
