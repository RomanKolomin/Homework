left_num = input('Введите шифр: ')
left_num_possible_options = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
left_num_correct = True
possible_pairs = []

# Checking if left_num is correct and making it int
try:
    left_num = int(left_num)
except ValueError:
    left_num_correct = False
if left_num not in left_num_possible_options or left_num_correct == False:
    print(f'Шифр: "{left_num}" введён неверно!')
else:
    left_num = int(left_num)

# Making lists of pairs
for i in range(1, max(left_num_possible_options)):
    for j in range(1, max(left_num_possible_options)):
        if (
                i + j == left_num
                and i != j
                and [j, i] not in possible_pairs
        ):
            possible_pairs.append([i, j])

# Making code from pairs


print(*possible_pairs)