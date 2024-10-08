left_num = input('Введите шифр: ')
left_num_possible_options = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
left_num_correct = True
possible_pairs = []
code = []

# Checking if left_num correct and making it int
try:
    left_num = int(left_num)
except ValueError:
    left_num_correct = False
if left_num not in left_num_possible_options or left_num_correct is False:
    print(f'Шифр: "{left_num}" введён неверно!')
else:
    left_num = int(left_num)

# Making lists of pairs
    for i in range(1, max(left_num_possible_options)):
        for j in range(1, max(left_num_possible_options)):
            if (
                    left_num % (i + j) == 0
                    and i != j
                    and [j, i] not in possible_pairs
            ):
                possible_pairs.append([i, j])

# Making code from pairs
    for i in range(len(possible_pairs)):
        code.append(int(''.join(map(str, possible_pairs[i]))))
    code = int(''.join(map(str, code)))

    print()
    print('Введенный шифр: ', left_num)
    print('Пары чисел: ', possible_pairs)
    print('Введите пароль: ', code)
