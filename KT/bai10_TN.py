def My_function(integers, number):
    # Your code here: Thuc hien duyet tung phan tu trong integers, so sanh tung phan tu voi number, neu bang nhau tra ve True, khac nhau tra ve False
    # vi du: integers = [1, 2, 3], number = 2, ban se tao ra list [False, True, False]
    check = False

    for i in integers:
        if i != number:
            continue
        else:
            check = True
            break
    return check

my_list = [1, 3, 9, 4]
assert My_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(My_function(my_list, 2))