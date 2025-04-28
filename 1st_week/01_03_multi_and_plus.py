#
def multi_and_plus(array):
    max = 0
    for num in array:
        plus_max_and_num = max + num
        multi_max_and_num = max * num
        if plus_max_and_num < multi_max_and_num:
            max = multi_max_and_num
        else:
            max = plus_max_and_num
    return max

print(multi_and_plus([0,3,5,6,1,2,4]))
print(multi_and_plus([3,2,1,5,9,7,4]))
print(multi_and_plus([1,1,1,3,3,2,5]))