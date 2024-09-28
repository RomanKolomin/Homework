# def get_multiplied_digits(number):
#     str_number = str(number)
#     first = int(str_number[0])
#     if int(str_number) == 0:
#         return 1
#     elif len(str_number) > 1:
#         return first * get_multiplied_digits(int(str_number[1:]))
#     else:
#         return first


def get_multiplied_digits(number):
    if number == 0:
        return 1
    elif len(str(number)) > 1:
        return int(str(number)[0]) * get_multiplied_digits(int(str(number)[1:]))
    else:
        return int(str(number)[0])


result = get_multiplied_digits(40203)
print(result)
