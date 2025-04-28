
def find_all_prime_under_number(number):
    flag = 2
    result = []
    while flag < number:
        count = 2
        prime_flag = True
        while count < flag:
            if flag % count == 0:
                prime_flag = False
                break
            count += 1
        if prime_flag:
            result.append(flag)
        flag += 1
    return result



print(find_all_prime_under_number(20))