def find_max_num(array):
    # for number in array:
    #     is_max_num = True
    #     for compare_number in array:
    #         if number < compare_number:
    #             is_max_num = False
    #     if is_max_num:
    #         return number

    for num in array:
        is_max_num = True
        for compare_num in array:
            if num < compare_num:
                is_max_num = False
        if is_max_num:
            print("최고 숫자는 ...", num)
            return num

print(find_max_num([3, 5, 6, 1, 2, 4]))

def find_max_num_2(array):
    max_num = -1
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

print(find_max_num_2([3, 5, 6, 1, 2, 4]))


