my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
current_position = 0

while current_position < len(my_list):
    if my_list[current_position] > 0:
        print(my_list[current_position])
    elif my_list[current_position] < 0:
        break
    current_position = current_position + 1